# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
import logging
import asyncio

import sys
from datetime import datetime, timedelta

from azure.core.pipeline.transport import AioHttpTransport
from multidict import CIMultiDict, CIMultiDictProxy

from azure.storage.blob.aio import (
    BlobServiceClient,
    ContainerClient,
    BlobClient,
)
from devtools_testutils import ResourceGroupPreparer, StorageAccountPreparer
from azure.storage.blob import (
    ContainerSasPermissions,
    BlobSasPermissions,
)

from azure.storage.blob._shared.shared_access_signature import QueryStringConstants

from testcase import (
    LogCaptured, GlobalStorageAccountPreparer
)
from asyncblobtestcase import (
    AsyncBlobTestCase,
)


if sys.version_info >= (3,):
    from urllib.parse import parse_qs, quote
else:
    from urlparse import parse_qs
    from urllib2 import quote

_AUTHORIZATION_HEADER_NAME = 'Authorization'


class AiohttpTestTransport(AioHttpTransport):
    """Workaround to vcrpy bug: https://github.com/kevin1024/vcrpy/pull/461
    """
    async def send(self, request, **config):
        response = await super(AiohttpTestTransport, self).send(request, **config)
        if not isinstance(response.headers, CIMultiDictProxy):
            response.headers = CIMultiDictProxy(CIMultiDict(response.internal_response.headers))
            response.content_type = response.headers.get("content-type")
        return response


class StorageLoggingTestAsync(AsyncBlobTestCase):
    async def _setup(self, bsc):
        self.container_name = self.get_resource_name('utcontainer')
        if self.is_live:
            try:
                # create source blob to be copied from
                self.source_blob_name = self.get_resource_name('srcblob')
                self.source_blob_data = self.get_random_bytes(4 * 1024)
                source_blob = bsc.get_blob_client(self.container_name, self.source_blob_name)

                await bsc.create_container(self.container_name)
                await source_blob.upload_blob(self.source_blob_data)

                # generate a SAS so that it is accessible with a URL
                sas_token = source_blob.generate_shared_access_signature(
                    permission=BlobSasPermissions(read=True),
                    expiry=datetime.utcnow() + timedelta(hours=1),
                )
                sas_source = BlobClient.from_blob_url(source_blob.url, credential=sas_token)
                self.source_blob_url = sas_source.url
            except:
                pass

    @GlobalStorageAccountPreparer()
    @AsyncBlobTestCase.await_prepared_test
    async def test_authorization_is_scrubbed_off(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        await self._setup(bsc)
        # Arrange
        container = bsc.get_container_client(self.container_name)
        # Act
        with LogCaptured(self) as log_captured:
            await container.get_container_properties(logging_enable=True)
            log_as_str = log_captured.getvalue()
            # Assert
            # make sure authorization header is logged, but its value is not
            # the keyword SharedKey is present in the authorization header's value
            self.assertTrue(_AUTHORIZATION_HEADER_NAME in log_as_str)
            self.assertFalse('SharedKey' in log_as_str)

    @GlobalStorageAccountPreparer()
    @AsyncBlobTestCase.await_prepared_test
    async def test_sas_signature_is_scrubbed_off(self, resource_group, location, storage_account, storage_account_key):
        # Test can only run live
        if not self.is_live:
            return

        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key)
        await self._setup(bsc)
        # Arrange
        container = bsc.get_container_client(self.container_name)
        token = container.generate_shared_access_signature(
            permission=ContainerSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=1),
        )
        # parse out the signed signature
        token_components = parse_qs(token)
        signed_signature = quote(token_components[QueryStringConstants.SIGNED_SIGNATURE][0])

        sas_service = ContainerClient.from_container_url(container.url, credential=token)

        # Act
        with LogCaptured(self) as log_captured:
            await sas_service.get_account_information(logging_enable=True)
            log_as_str = log_captured.getvalue()

            # Assert
            # make sure the query parameter 'sig' is logged, but its value is not
            self.assertTrue(QueryStringConstants.SIGNED_SIGNATURE in log_as_str)
            self.assertFalse(signed_signature in log_as_str)

    @GlobalStorageAccountPreparer()
    @AsyncBlobTestCase.await_prepared_test
    async def test_copy_source_sas_is_scrubbed_off(self, resource_group, location, storage_account, storage_account_key):
        # Test can only run live
        if not self.is_live:
            return
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key)
        await self._setup(bsc)
        # Arrange
        dest_blob_name = self.get_resource_name('destblob')
        dest_blob = bsc.get_blob_client(self.container_name, dest_blob_name)

        # parse out the signed signature
        token_components = parse_qs(self.source_blob_url)
        signed_signature = quote(token_components[QueryStringConstants.SIGNED_SIGNATURE][0])

        # Act
        with LogCaptured(self) as log_captured:
            await dest_blob.start_copy_from_url(
                self.source_blob_url, requires_sync=True, logging_enable=True)
            log_as_str = log_captured.getvalue()

            # Assert
            # make sure the query parameter 'sig' is logged, but its value is not
            self.assertTrue(QueryStringConstants.SIGNED_SIGNATURE in log_as_str)
            self.assertFalse(signed_signature in log_as_str)

            # make sure authorization header is logged, but its value is not
            # the keyword SharedKey is present in the authorization header's value
            self.assertTrue(_AUTHORIZATION_HEADER_NAME in log_as_str)
            self.assertFalse('SharedKey' in log_as_str)

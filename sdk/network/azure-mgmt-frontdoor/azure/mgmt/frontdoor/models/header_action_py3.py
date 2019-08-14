# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HeaderAction(Model):
    """An action that can manipulate an http header.

    All required parameters must be populated in order to send to Azure.

    :param header_action_type: Required. Which type of manipulation to apply
     to the header. Possible values include: 'Append', 'Delete', 'Overwrite'
    :type header_action_type: str or
     ~azure.mgmt.frontdoor.models.HeaderActionType
    :param header_name: Required. The name of the header this action will
     apply to.
    :type header_name: str
    :param value: The value to update the given header name with. This value
     is not used if the actionType is Delete.
    :type value: str
    """

    _validation = {
        'header_action_type': {'required': True},
        'header_name': {'required': True},
    }

    _attribute_map = {
        'header_action_type': {'key': 'headerActionType', 'type': 'str'},
        'header_name': {'key': 'headerName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, header_action_type, header_name: str, value: str=None, **kwargs) -> None:
        super(HeaderAction, self).__init__(**kwargs)
        self.header_action_type = header_action_type
        self.header_name = header_name
        self.value = value

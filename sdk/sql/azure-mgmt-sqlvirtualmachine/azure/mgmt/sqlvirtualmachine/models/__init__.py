# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AdditionalFeaturesServerConfigurations
    from ._models_py3 import AutoBackupSettings
    from ._models_py3 import AutoPatchingSettings
    from ._models_py3 import AvailabilityGroupListener
    from ._models_py3 import AvailabilityGroupListenerListResult
    from ._models_py3 import KeyVaultCredentialSettings
    from ._models_py3 import LoadBalancerConfiguration
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PrivateIPAddress
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import ResourceIdentity
    from ._models_py3 import SQLStorageSettings
    from ._models_py3 import ServerConfigurationsManagementSettings
    from ._models_py3 import SqlConnectivityUpdateSettings
    from ._models_py3 import SqlStorageUpdateSettings
    from ._models_py3 import SqlVirtualMachine
    from ._models_py3 import SqlVirtualMachineGroup
    from ._models_py3 import SqlVirtualMachineGroupListResult
    from ._models_py3 import SqlVirtualMachineGroupUpdate
    from ._models_py3 import SqlVirtualMachineListResult
    from ._models_py3 import SqlVirtualMachineUpdate
    from ._models_py3 import SqlWorkloadTypeUpdateSettings
    from ._models_py3 import StorageConfigurationSettings
    from ._models_py3 import TrackedResource
    from ._models_py3 import WsfcDomainCredentials
    from ._models_py3 import WsfcDomainProfile
except (SyntaxError, ImportError):
    from ._models import AdditionalFeaturesServerConfigurations  # type: ignore
    from ._models import AutoBackupSettings  # type: ignore
    from ._models import AutoPatchingSettings  # type: ignore
    from ._models import AvailabilityGroupListener  # type: ignore
    from ._models import AvailabilityGroupListenerListResult  # type: ignore
    from ._models import KeyVaultCredentialSettings  # type: ignore
    from ._models import LoadBalancerConfiguration  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PrivateIPAddress  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceIdentity  # type: ignore
    from ._models import SQLStorageSettings  # type: ignore
    from ._models import ServerConfigurationsManagementSettings  # type: ignore
    from ._models import SqlConnectivityUpdateSettings  # type: ignore
    from ._models import SqlStorageUpdateSettings  # type: ignore
    from ._models import SqlVirtualMachine  # type: ignore
    from ._models import SqlVirtualMachineGroup  # type: ignore
    from ._models import SqlVirtualMachineGroupListResult  # type: ignore
    from ._models import SqlVirtualMachineGroupUpdate  # type: ignore
    from ._models import SqlVirtualMachineListResult  # type: ignore
    from ._models import SqlVirtualMachineUpdate  # type: ignore
    from ._models import SqlWorkloadTypeUpdateSettings  # type: ignore
    from ._models import StorageConfigurationSettings  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import WsfcDomainCredentials  # type: ignore
    from ._models import WsfcDomainProfile  # type: ignore

from ._sql_virtual_machine_management_client_enums import (
    BackupScheduleType,
    ClusterConfiguration,
    ClusterManagerType,
    ConnectivityType,
    DayOfWeek,
    DiskConfigurationType,
    FullBackupFrequencyType,
    IdentityType,
    OperationOrigin,
    ScaleType,
    SqlImageSku,
    SqlManagementMode,
    SqlServerLicenseType,
    SqlVmGroupImageSku,
    SqlWorkloadType,
    StorageWorkloadType,
)

__all__ = [
    'AdditionalFeaturesServerConfigurations',
    'AutoBackupSettings',
    'AutoPatchingSettings',
    'AvailabilityGroupListener',
    'AvailabilityGroupListenerListResult',
    'KeyVaultCredentialSettings',
    'LoadBalancerConfiguration',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PrivateIPAddress',
    'ProxyResource',
    'Resource',
    'ResourceIdentity',
    'SQLStorageSettings',
    'ServerConfigurationsManagementSettings',
    'SqlConnectivityUpdateSettings',
    'SqlStorageUpdateSettings',
    'SqlVirtualMachine',
    'SqlVirtualMachineGroup',
    'SqlVirtualMachineGroupListResult',
    'SqlVirtualMachineGroupUpdate',
    'SqlVirtualMachineListResult',
    'SqlVirtualMachineUpdate',
    'SqlWorkloadTypeUpdateSettings',
    'StorageConfigurationSettings',
    'TrackedResource',
    'WsfcDomainCredentials',
    'WsfcDomainProfile',
    'BackupScheduleType',
    'ClusterConfiguration',
    'ClusterManagerType',
    'ConnectivityType',
    'DayOfWeek',
    'DiskConfigurationType',
    'FullBackupFrequencyType',
    'IdentityType',
    'OperationOrigin',
    'ScaleType',
    'SqlImageSku',
    'SqlManagementMode',
    'SqlServerLicenseType',
    'SqlVmGroupImageSku',
    'SqlWorkloadType',
    'StorageWorkloadType',
]

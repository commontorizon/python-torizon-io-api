# coding: utf-8

# flake8: noqa
"""
    Torizon OTA

     This API is rate limited and will return the following headers for each API call.    - X-RateLimit-Limit - The total number of requests allowed within a time period   - X-RateLimit-Remaining - The total number of requests still allowed until the end of the rate limiting period   - X-RateLimit-Reset - The number of seconds until the limit is fully reset  In addition, if an API client is rate limited, it will receive a HTTP 420 response with the following header:     - Retry-After - The number of seconds to wait until this request is allowed  

    The version of the OpenAPI document: 2.0-Beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from torizon_io_api.models.bad_request_repr import BadRequestRepr
from torizon_io_api.models.client_signature import ClientSignature
from torizon_io_api.models.conflict_repr import ConflictRepr
from torizon_io_api.models.create_fleet import CreateFleet
from torizon_io_api.models.create_lockbox_request import CreateLockboxRequest
from torizon_io_api.models.custom_update_data import CustomUpdateData
from torizon_io_api.models.delegation_info import DelegationInfo
from torizon_io_api.models.device_create_req import DeviceCreateReq
from torizon_io_api.models.device_info_basic import DeviceInfoBasic
from torizon_io_api.models.device_info_extended import DeviceInfoExtended
from torizon_io_api.models.device_package import DevicePackage
from torizon_io_api.models.device_packages import DevicePackages
from torizon_io_api.models.device_sort import DeviceSort
from torizon_io_api.models.device_sort_direction import DeviceSortDirection
from torizon_io_api.models.device_status import DeviceStatus
from torizon_io_api.models.ecu_info_image import EcuInfoImage
from torizon_io_api.models.ecu_info_response import EcuInfoResponse
from torizon_io_api.models.edit_package import EditPackage
from torizon_io_api.models.error_representation import ErrorRepresentation
from torizon_io_api.models.external_package import ExternalPackage
from torizon_io_api.models.file_info import FileInfo
from torizon_io_api.models.fleet import Fleet
from torizon_io_api.models.fleet_type import FleetType
from torizon_io_api.models.image import Image
from torizon_io_api.models.installed_package import InstalledPackage
from torizon_io_api.models.json_signed_payload import JsonSignedPayload
from torizon_io_api.models.metrics_response import MetricsResponse
from torizon_io_api.models.network_info import NetworkInfo
from torizon_io_api.models.not_found_repr import NotFoundRepr
from torizon_io_api.models.package import Package
from torizon_io_api.models.package_info import PackageInfo
from torizon_io_api.models.pagination_result_device_info_basic import PaginationResultDeviceInfoBasic
from torizon_io_api.models.pagination_result_device_packages import PaginationResultDevicePackages
from torizon_io_api.models.pagination_result_external_package import PaginationResultExternalPackage
from torizon_io_api.models.pagination_result_fleet import PaginationResultFleet
from torizon_io_api.models.pagination_result_network_info import PaginationResultNetworkInfo
from torizon_io_api.models.pagination_result_package import PaginationResultPackage
from torizon_io_api.models.pagination_result_string import PaginationResultString
from torizon_io_api.models.provision_info import ProvisionInfo
from torizon_io_api.models.queue_response import QueueResponse
from torizon_io_api.models.range_not_satisfiable_repr import RangeNotSatisfiableRepr
from torizon_io_api.models.series import Series
from torizon_io_api.models.series_meta import SeriesMeta
from torizon_io_api.models.signature_method import SignatureMethod
from torizon_io_api.models.simple_device_info import SimpleDeviceInfo
from torizon_io_api.models.simple_device_not_affected_info import SimpleDeviceNotAffectedInfo
from torizon_io_api.models.sort_direction import SortDirection
from torizon_io_api.models.target_image import TargetImage
from torizon_io_api.models.target_items_sort import TargetItemsSort
from torizon_io_api.models.time_aggregation import TimeAggregation
from torizon_io_api.models.time_aggregation_method import TimeAggregationMethod
from torizon_io_api.models.tuple2_device_tag_id_device_tag_value import Tuple2DeviceTagIdDeviceTagValue
from torizon_io_api.models.tuple2_long_option_double import Tuple2LongOptionDouble
from torizon_io_api.models.update_create_result import UpdateCreateResult
from torizon_io_api.models.update_fleet import UpdateFleet
from torizon_io_api.models.update_hibernation_status_request import UpdateHibernationStatusRequest
from torizon_io_api.models.update_request import UpdateRequest
from torizon_io_api.models.upstream_endpoint_error_repr import UpstreamEndpointErrorRepr

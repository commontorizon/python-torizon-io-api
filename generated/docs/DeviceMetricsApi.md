# torizon_io_api.DeviceMetricsApi

All URIs are relative to *https://app.torizon.io/api/v2beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_data_devices_deviceuuid_metrics**](DeviceMetricsApi.md#get_device_data_devices_deviceuuid_metrics) | **GET** /device-data/devices/{deviceUuid}/metrics | Get metrics data from a single device
[**get_device_data_fleets_fleetid_metrics**](DeviceMetricsApi.md#get_device_data_fleets_fleetid_metrics) | **GET** /device-data/fleets/{fleetId}/metrics | Get aggregated metrics data from a fleet of devices
[**get_device_data_metric_names**](DeviceMetricsApi.md#get_device_data_metric_names) | **GET** /device-data/metric-names | Get the list of metrics available in your repository


# **get_device_data_devices_deviceuuid_metrics**
> MetricsResponse get_device_data_devices_deviceuuid_metrics(device_uuid, var_from, to, metric=metric, resolution=resolution)

Get metrics data from a single device

 This endpoint will return time-bucketed data as reported by the specified device. You must specify a time interval in  Unix Epoch milliseconds via the `from` and `to` query parameters.  You can optionally specify one or more metrics in the query parameter (e.g. `metrics=metric1&metrics=metrics2`, etc.  OR `metrics[]=metric1,metrics2`, etc.). If you do not specify, you will get all metrics available in the repository.  You can also specify a `resolution`. This parameter defaults to 200, with a maximum permitted value of 2000, and  determines the granularity of the data returned. The data returned will be separated into buckets, with each bucket  representing the mean value of the data returned during that period.  For example, suppose you have a device reporting its CPU temperature every minute. You request that metric, with a  resolution of 24 and a time interval that is 1 day long. You will get back 24 data points, each representing a one-hour slice of time. The value returned for each one-hour slice will be the average of the 60 reported  measurements that the device sent during that hour.         

### Example

* Bearer Authentication (BearerAuth):

```python
import torizon_io_api
from torizon_io_api.models.metrics_response import MetricsResponse
from torizon_io_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.torizon.io/api/v2beta
# See configuration.py for a list of all supported configuration parameters.
configuration = torizon_io_api.Configuration(
    host = "https://app.torizon.io/api/v2beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = torizon_io_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torizon_io_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torizon_io_api.DeviceMetricsApi(api_client)
    device_uuid = 'device_uuid_example' # str | 
    var_from = 56 # int | 
    to = 56 # int | 
    metric = ['metric_example'] # List[str] |  (optional)
    resolution = 56 # int |  (optional)

    try:
        # Get metrics data from a single device
        api_response = api_instance.get_device_data_devices_deviceuuid_metrics(device_uuid, var_from, to, metric=metric, resolution=resolution)
        print("The response of DeviceMetricsApi->get_device_data_devices_deviceuuid_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceMetricsApi->get_device_data_devices_deviceuuid_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**|  | 
 **var_from** | **int**|  | 
 **to** | **int**|  | 
 **metric** | [**List[str]**](str.md)|  | [optional] 
 **resolution** | **int**|  | [optional] 

### Return type

[**MetricsResponse**](MetricsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**404** | Resource Not Found |  -  |
**416** | Range not Satisfiable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_data_fleets_fleetid_metrics**
> MetricsResponse get_device_data_fleets_fleetid_metrics(fleet_id, var_from, to, metric=metric, resolution=resolution)

Get aggregated metrics data from a fleet of devices

 This endpoint will return aggregated time-bucketed data as reported by the devices in the specified fleet. You must  specify a time interval in Unix Epoch milliseconds via the `from` and `to` query parameters.   You can also specify a `resolution`. This parameter defaults to 200, with a maximum permitted value of 2000, and  determines the granularity of the data returned. The data returned will be separated into buckets, with each bucket  representing the aggregated data from the period. For example, if you specify a one day long time interval with a resolution of 24, you will get 24 buckets, each representing a one hour slice of the day. If you request a resolution  of 48, your buckets will be 30 minutes long.  You also must specify one or more metrics as query parameters (e.g. `metrics=metric1&metrics=metrics2`, etc. OR  `metrics[]=metric1,metrics2`, etc.). For each metric you specify, you will get back four different series of datapoints:   * `{metric}-count` reports how many devices in the fleet actually reported data during this time interval. * `{metric}-avg` reports the average value of all reported values for the metric in the period. Note that the average  is over the number of devices that reported data: devices that didn't report the metric during the interval will not be reflected in this datapoint. * `{metric}-max` gives the highest value reported by a device in the specified interval * `{metric}-min` gives the lowest value reported by a device in the specified interval         

### Example

* Bearer Authentication (BearerAuth):

```python
import torizon_io_api
from torizon_io_api.models.metrics_response import MetricsResponse
from torizon_io_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.torizon.io/api/v2beta
# See configuration.py for a list of all supported configuration parameters.
configuration = torizon_io_api.Configuration(
    host = "https://app.torizon.io/api/v2beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = torizon_io_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torizon_io_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torizon_io_api.DeviceMetricsApi(api_client)
    fleet_id = 'fleet_id_example' # str | 
    var_from = 56 # int | 
    to = 56 # int | 
    metric = ['metric_example'] # List[str] |  (optional)
    resolution = 56 # int |  (optional)

    try:
        # Get aggregated metrics data from a fleet of devices
        api_response = api_instance.get_device_data_fleets_fleetid_metrics(fleet_id, var_from, to, metric=metric, resolution=resolution)
        print("The response of DeviceMetricsApi->get_device_data_fleets_fleetid_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceMetricsApi->get_device_data_fleets_fleetid_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **str**|  | 
 **var_from** | **int**|  | 
 **to** | **int**|  | 
 **metric** | [**List[str]**](str.md)|  | [optional] 
 **resolution** | **int**|  | [optional] 

### Return type

[**MetricsResponse**](MetricsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**416** | Range not Satisfiable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_data_metric_names**
> PaginationResultString get_device_data_metric_names(var_from=var_from, to=to)

Get the list of metrics available in your repository

 Lists the metrics available in your repository.  In the default TorizonCore configuration, devices will report certain default metrics. You can also add your own metrics, as described in the [TorizonCore documentation](https://developer.toradex.com/torizon/torizon-platform/device-monitoring-in-torizoncore/#customizing-device-metrics-for-torizon-platform). Calling this endpoint will give you the list of valid metric names for your repository; generally this will include the default set plus any that you have defined yourself.  You can optionally specify a time interval in Unix Epoch milliseconds via the `from` and `to` query parameters. This will return the list of metrics reported by devices in your repository during that specific interval.         

### Example

* Bearer Authentication (BearerAuth):

```python
import torizon_io_api
from torizon_io_api.models.pagination_result_string import PaginationResultString
from torizon_io_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.torizon.io/api/v2beta
# See configuration.py for a list of all supported configuration parameters.
configuration = torizon_io_api.Configuration(
    host = "https://app.torizon.io/api/v2beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = torizon_io_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with torizon_io_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = torizon_io_api.DeviceMetricsApi(api_client)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)

    try:
        # Get the list of metrics available in your repository
        api_response = api_instance.get_device_data_metric_names(var_from=var_from, to=to)
        print("The response of DeviceMetricsApi->get_device_data_metric_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceMetricsApi->get_device_data_metric_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 

### Return type

[**PaginationResultString**](PaginationResultString.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**404** | Resource Not Found |  -  |
**416** | Range not Satisfiable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


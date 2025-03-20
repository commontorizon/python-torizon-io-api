# PaginationResultDeviceInfoBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[DeviceInfoBasic]**](DeviceInfoBasic.md) |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from torizon_io_api.models.pagination_result_device_info_basic import PaginationResultDeviceInfoBasic

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultDeviceInfoBasic from a JSON string
pagination_result_device_info_basic_instance = PaginationResultDeviceInfoBasic.from_json(json)
# print the JSON string representation of the object
print(PaginationResultDeviceInfoBasic.to_json())

# convert the object into a dict
pagination_result_device_info_basic_dict = pagination_result_device_info_basic_instance.to_dict()
# create an instance of PaginationResultDeviceInfoBasic from a dict
pagination_result_device_info_basic_from_dict = PaginationResultDeviceInfoBasic.from_dict(pagination_result_device_info_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



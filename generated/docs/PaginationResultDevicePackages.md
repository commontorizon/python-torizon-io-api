# PaginationResultDevicePackages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[DevicePackages]**](DevicePackages.md) |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from torizon_io_api.models.pagination_result_device_packages import PaginationResultDevicePackages

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultDevicePackages from a JSON string
pagination_result_device_packages_instance = PaginationResultDevicePackages.from_json(json)
# print the JSON string representation of the object
print(PaginationResultDevicePackages.to_json())

# convert the object into a dict
pagination_result_device_packages_dict = pagination_result_device_packages_instance.to_dict()
# create an instance of PaginationResultDevicePackages from a dict
pagination_result_device_packages_from_dict = PaginationResultDevicePackages.from_dict(pagination_result_device_packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



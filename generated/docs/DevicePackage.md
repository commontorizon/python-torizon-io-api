# DevicePackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 
**checksum** | **str** |  | 

## Example

```python
from torizon_io_api.models.device_package import DevicePackage

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePackage from a JSON string
device_package_instance = DevicePackage.from_json(json)
# print the JSON string representation of the object
print(DevicePackage.to_json())

# convert the object into a dict
device_package_dict = device_package_instance.to_dict()
# create an instance of DevicePackage from a dict
device_package_from_dict = DevicePackage.from_dict(device_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DevicePackages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **str** |  | 
**installed_packages** | [**List[InstalledPackage]**](InstalledPackage.md) |  | [optional] 

## Example

```python
from torizon_io_api.models.device_packages import DevicePackages

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePackages from a JSON string
device_packages_instance = DevicePackages.from_json(json)
# print the JSON string representation of the object
print(DevicePackages.to_json())

# convert the object into a dict
device_packages_dict = device_packages_instance.to_dict()
# create an instance of DevicePackages from a dict
device_packages_from_dict = DevicePackages.from_dict(device_packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



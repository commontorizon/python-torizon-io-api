# SimpleDeviceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **str** |  | 
**device_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from torizon_io_api.models.simple_device_info import SimpleDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDeviceInfo from a JSON string
simple_device_info_instance = SimpleDeviceInfo.from_json(json)
# print the JSON string representation of the object
print(SimpleDeviceInfo.to_json())

# convert the object into a dict
simple_device_info_dict = simple_device_info_instance.to_dict()
# create an instance of SimpleDeviceInfo from a dict
simple_device_info_from_dict = SimpleDeviceInfo.from_dict(simple_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



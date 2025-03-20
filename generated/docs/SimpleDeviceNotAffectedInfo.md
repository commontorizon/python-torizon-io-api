# SimpleDeviceNotAffectedInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **str** |  | 
**device_id** | **str** |  | 
**name** | **str** |  | 
**ecu_errors** | [**Dict[str, ErrorRepresentation]**](ErrorRepresentation.md) |  | 

## Example

```python
from torizon_io_api.models.simple_device_not_affected_info import SimpleDeviceNotAffectedInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDeviceNotAffectedInfo from a JSON string
simple_device_not_affected_info_instance = SimpleDeviceNotAffectedInfo.from_json(json)
# print the JSON string representation of the object
print(SimpleDeviceNotAffectedInfo.to_json())

# convert the object into a dict
simple_device_not_affected_info_dict = simple_device_not_affected_info_instance.to_dict()
# create an instance of SimpleDeviceNotAffectedInfo from a dict
simple_device_not_affected_info_from_dict = SimpleDeviceNotAffectedInfo.from_dict(simple_device_not_affected_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



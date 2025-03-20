# DeviceCreateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** |  | [optional] 
**device_id** | **str** |  | 
**hibernated** | **bool** |  | [optional] 
**fleet_ids** | **List[str]** |  | [optional] 

## Example

```python
from torizon_io_api.models.device_create_req import DeviceCreateReq

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCreateReq from a JSON string
device_create_req_instance = DeviceCreateReq.from_json(json)
# print the JSON string representation of the object
print(DeviceCreateReq.to_json())

# convert the object into a dict
device_create_req_dict = device_create_req_instance.to_dict()
# create an instance of DeviceCreateReq from a dict
device_create_req_from_dict = DeviceCreateReq.from_dict(device_create_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



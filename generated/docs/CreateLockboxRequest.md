# CreateLockboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_ids** | **List[str]** |  | [optional] 
**custom** | [**Dict[str, CustomUpdateData]**](CustomUpdateData.md) |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from torizon_io_api.models.create_lockbox_request import CreateLockboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLockboxRequest from a JSON string
create_lockbox_request_instance = CreateLockboxRequest.from_json(json)
# print the JSON string representation of the object
print(CreateLockboxRequest.to_json())

# convert the object into a dict
create_lockbox_request_dict = create_lockbox_request_instance.to_dict()
# create an instance of CreateLockboxRequest from a dict
create_lockbox_request_from_dict = CreateLockboxRequest.from_dict(create_lockbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



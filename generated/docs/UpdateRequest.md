# UpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_ids** | **List[str]** |  | [optional] 
**custom** | [**Dict[str, CustomUpdateData]**](CustomUpdateData.md) |  | [optional] 
**devices** | **List[str]** |  | [optional] 
**fleets** | **List[str]** |  | [optional] 

## Example

```python
from torizon_io_api.models.update_request import UpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRequest from a JSON string
update_request_instance = UpdateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRequest.to_json())

# convert the object into a dict
update_request_dict = update_request_instance.to_dict()
# create an instance of UpdateRequest from a dict
update_request_from_dict = UpdateRequest.from_dict(update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



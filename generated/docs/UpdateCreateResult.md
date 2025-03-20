# UpdateCreateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[SimpleDeviceInfo]**](SimpleDeviceInfo.md) |  | [optional] 
**not_affected** | [**List[SimpleDeviceNotAffectedInfo]**](SimpleDeviceNotAffectedInfo.md) |  | [optional] 

## Example

```python
from torizon_io_api.models.update_create_result import UpdateCreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCreateResult from a JSON string
update_create_result_instance = UpdateCreateResult.from_json(json)
# print the JSON string representation of the object
print(UpdateCreateResult.to_json())

# convert the object into a dict
update_create_result_dict = update_create_result_instance.to_dict()
# create an instance of UpdateCreateResult from a dict
update_create_result_from_dict = UpdateCreateResult.from_dict(update_create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



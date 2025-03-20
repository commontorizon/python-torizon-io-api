# UpdateHibernationStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | 

## Example

```python
from torizon_io_api.models.update_hibernation_status_request import UpdateHibernationStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHibernationStatusRequest from a JSON string
update_hibernation_status_request_instance = UpdateHibernationStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateHibernationStatusRequest.to_json())

# convert the object into a dict
update_hibernation_status_request_dict = update_hibernation_status_request_instance.to_dict()
# create an instance of UpdateHibernationStatusRequest from a dict
update_hibernation_status_request_from_dict = UpdateHibernationStatusRequest.from_dict(update_hibernation_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DelegationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_fetched** | **datetime** |  | [optional] 
**remote_uri** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**expires** | **datetime** |  | [optional] 

## Example

```python
from torizon_io_api.models.delegation_info import DelegationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DelegationInfo from a JSON string
delegation_info_instance = DelegationInfo.from_json(json)
# print the JSON string representation of the object
print(DelegationInfo.to_json())

# convert the object into a dict
delegation_info_dict = delegation_info_instance.to_dict()
# create an instance of DelegationInfo from a dict
delegation_info_from_dict = DelegationInfo.from_dict(delegation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



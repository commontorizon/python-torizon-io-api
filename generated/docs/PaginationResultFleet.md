# PaginationResultFleet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Fleet]**](Fleet.md) |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from torizon_io_api.models.pagination_result_fleet import PaginationResultFleet

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultFleet from a JSON string
pagination_result_fleet_instance = PaginationResultFleet.from_json(json)
# print the JSON string representation of the object
print(PaginationResultFleet.to_json())

# convert the object into a dict
pagination_result_fleet_dict = pagination_result_fleet_instance.to_dict()
# create an instance of PaginationResultFleet from a dict
pagination_result_fleet_from_dict = PaginationResultFleet.from_dict(pagination_result_fleet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



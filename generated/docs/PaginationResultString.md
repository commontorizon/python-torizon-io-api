# PaginationResultString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from torizon_io_api.models.pagination_result_string import PaginationResultString

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultString from a JSON string
pagination_result_string_instance = PaginationResultString.from_json(json)
# print the JSON string representation of the object
print(PaginationResultString.to_json())

# convert the object into a dict
pagination_result_string_dict = pagination_result_string_instance.to_dict()
# create an instance of PaginationResultString from a dict
pagination_result_string_from_dict = PaginationResultString.from_dict(pagination_result_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



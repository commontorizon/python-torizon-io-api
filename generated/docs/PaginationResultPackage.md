# PaginationResultPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Package]**](Package.md) |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from torizon_io_api.models.pagination_result_package import PaginationResultPackage

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultPackage from a JSON string
pagination_result_package_instance = PaginationResultPackage.from_json(json)
# print the JSON string representation of the object
print(PaginationResultPackage.to_json())

# convert the object into a dict
pagination_result_package_dict = pagination_result_package_instance.to_dict()
# create an instance of PaginationResultPackage from a dict
pagination_result_package_from_dict = PaginationResultPackage.from_dict(pagination_result_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PaginationResultExternalPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ExternalPackage]**](ExternalPackage.md) |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from torizon_io_api.models.pagination_result_external_package import PaginationResultExternalPackage

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultExternalPackage from a JSON string
pagination_result_external_package_instance = PaginationResultExternalPackage.from_json(json)
# print the JSON string representation of the object
print(PaginationResultExternalPackage.to_json())

# convert the object into a dict
pagination_result_external_package_dict = pagination_result_external_package_instance.to_dict()
# create an instance of PaginationResultExternalPackage from a dict
pagination_result_external_package_from_dict = PaginationResultExternalPackage.from_dict(pagination_result_external_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



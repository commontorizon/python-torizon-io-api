# EcuInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**hardware_id** | **str** |  | 
**primary** | **bool** |  | 
**image** | [**EcuInfoImage**](EcuInfoImage.md) |  | 

## Example

```python
from torizon_io_api.models.ecu_info_response import EcuInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EcuInfoResponse from a JSON string
ecu_info_response_instance = EcuInfoResponse.from_json(json)
# print the JSON string representation of the object
print(EcuInfoResponse.to_json())

# convert the object into a dict
ecu_info_response_dict = ecu_info_response_instance.to_dict()
# create an instance of EcuInfoResponse from a dict
ecu_info_response_from_dict = EcuInfoResponse.from_dict(ecu_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



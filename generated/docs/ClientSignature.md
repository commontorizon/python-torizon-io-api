# ClientSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyid** | **str** |  | 
**method** | [**SignatureMethod**](SignatureMethod.md) |  | 
**sig** | **str** |  | 

## Example

```python
from torizon_io_api.models.client_signature import ClientSignature

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSignature from a JSON string
client_signature_instance = ClientSignature.from_json(json)
# print the JSON string representation of the object
print(ClientSignature.to_json())

# convert the object into a dict
client_signature_dict = client_signature_instance.to_dict()
# create an instance of ClientSignature from a dict
client_signature_from_dict = ClientSignature.from_dict(client_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



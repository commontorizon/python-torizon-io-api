# JsonSignedPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signatures** | [**List[ClientSignature]**](ClientSignature.md) |  | [optional] 
**signed** | **object** |  | 

## Example

```python
from torizon_io_api.models.json_signed_payload import JsonSignedPayload

# TODO update the JSON string below
json = "{}"
# create an instance of JsonSignedPayload from a JSON string
json_signed_payload_instance = JsonSignedPayload.from_json(json)
# print the JSON string representation of the object
print(JsonSignedPayload.to_json())

# convert the object into a dict
json_signed_payload_dict = json_signed_payload_instance.to_dict()
# create an instance of JsonSignedPayload from a dict
json_signed_payload_from_dict = JsonSignedPayload.from_dict(json_signed_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# QueueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**targets** | [**Dict[str, TargetImage]**](TargetImage.md) |  | 
**in_flight** | **bool** |  | 

## Example

```python
from torizon_io_api.models.queue_response import QueueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueueResponse from a JSON string
queue_response_instance = QueueResponse.from_json(json)
# print the JSON string representation of the object
print(QueueResponse.to_json())

# convert the object into a dict
queue_response_dict = queue_response_instance.to_dict()
# create an instance of QueueResponse from a dict
queue_response_from_dict = QueueResponse.from_dict(queue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



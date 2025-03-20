# TimeAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**method** | [**TimeAggregationMethod**](TimeAggregationMethod.md) |  | 

## Example

```python
from torizon_io_api.models.time_aggregation import TimeAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAggregation from a JSON string
time_aggregation_instance = TimeAggregation.from_json(json)
# print the JSON string representation of the object
print(TimeAggregation.to_json())

# convert the object into a dict
time_aggregation_dict = time_aggregation_instance.to_dict()
# create an instance of TimeAggregation from a dict
time_aggregation_from_dict = TimeAggregation.from_dict(time_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



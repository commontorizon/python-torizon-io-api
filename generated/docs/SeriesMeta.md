# SeriesMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**TimeAggregation**](TimeAggregation.md) |  | 
**device_ids** | **List[str]** |  | [optional] 

## Example

```python
from torizon_io_api.models.series_meta import SeriesMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesMeta from a JSON string
series_meta_instance = SeriesMeta.from_json(json)
# print the JSON string representation of the object
print(SeriesMeta.to_json())

# convert the object into a dict
series_meta_dict = series_meta_instance.to_dict()
# create an instance of SeriesMeta from a dict
series_meta_from_dict = SeriesMeta.from_dict(series_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



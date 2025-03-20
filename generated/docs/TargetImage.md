# TargetImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**Image**](Image.md) |  | 
**uri** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from torizon_io_api.models.target_image import TargetImage

# TODO update the JSON string below
json = "{}"
# create an instance of TargetImage from a JSON string
target_image_instance = TargetImage.from_json(json)
# print the JSON string representation of the object
print(TargetImage.to_json())

# convert the object into a dict
target_image_dict = target_image_instance.to_dict()
# create an instance of TargetImage from a dict
target_image_from_dict = TargetImage.from_dict(target_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



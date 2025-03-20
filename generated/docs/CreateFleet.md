# CreateFleet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**fleet_type** | [**FleetType**](FleetType.md) |  | 
**expression** | **str** |  | [optional] 

## Example

```python
from torizon_io_api.models.create_fleet import CreateFleet

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFleet from a JSON string
create_fleet_instance = CreateFleet.from_json(json)
# print the JSON string representation of the object
print(CreateFleet.to_json())

# convert the object into a dict
create_fleet_dict = create_fleet_instance.to_dict()
# create an instance of CreateFleet from a dict
create_fleet_from_dict = CreateFleet.from_dict(create_fleet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



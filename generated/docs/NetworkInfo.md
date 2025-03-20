# NetworkInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **str** |  | 
**local_ip_v4** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 

## Example

```python
from torizon_io_api.models.network_info import NetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInfo from a JSON string
network_info_instance = NetworkInfo.from_json(json)
# print the JSON string representation of the object
print(NetworkInfo.to_json())

# convert the object into a dict
network_info_dict = network_info_instance.to_dict()
# create an instance of NetworkInfo from a dict
network_info_from_dict = NetworkInfo.from_dict(network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



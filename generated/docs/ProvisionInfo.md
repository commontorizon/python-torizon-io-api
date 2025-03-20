# ProvisionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**auto_prov_url** | **str** |  | 
**gateway_url** | **str** |  | 
**provisioned_devices** | **int** |  | 
**standard_device_limit** | **int** |  | 

## Example

```python
from torizon_io_api.models.provision_info import ProvisionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionInfo from a JSON string
provision_info_instance = ProvisionInfo.from_json(json)
# print the JSON string representation of the object
print(ProvisionInfo.to_json())

# convert the object into a dict
provision_info_dict = provision_info_instance.to_dict()
# create an instance of ProvisionInfo from a dict
provision_info_from_dict = ProvisionInfo.from_dict(provision_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



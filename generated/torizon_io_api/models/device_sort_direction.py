# coding: utf-8

"""
    Torizon OTA

     This API is rate limited and will return the following headers for each API call.    - X-RateLimit-Limit - The total number of requests allowed within a time period   - X-RateLimit-Remaining - The total number of requests still allowed until the end of the rate limiting period   - X-RateLimit-Reset - The number of seconds until the limit is fully reset  In addition, if an API client is rate limited, it will receive a HTTP 420 response with the following header:     - Retry-After - The number of seconds to wait until this request is allowed  

    The version of the OpenAPI document: 2.0-Beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DeviceSortDirection(str, Enum):
    """
    DeviceSortDirection
    """

    """
    allowed enum values
    """
    ASC = 'Asc'
    DESC = 'Desc'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeviceSortDirection from a JSON string"""
        return cls(json.loads(json_str))



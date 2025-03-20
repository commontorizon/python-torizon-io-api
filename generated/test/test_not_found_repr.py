# coding: utf-8

"""
    Torizon OTA

     This API is rate limited and will return the following headers for each API call.    - X-RateLimit-Limit - The total number of requests allowed within a time period   - X-RateLimit-Remaining - The total number of requests still allowed until the end of the rate limiting period   - X-RateLimit-Reset - The number of seconds until the limit is fully reset  In addition, if an API client is rate limited, it will receive a HTTP 420 response with the following header:     - Retry-After - The number of seconds to wait until this request is allowed  

    The version of the OpenAPI document: 2.0-Beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from torizon_io_api.models.not_found_repr import NotFoundRepr

class TestNotFoundRepr(unittest.TestCase):
    """NotFoundRepr unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotFoundRepr:
        """Test NotFoundRepr
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotFoundRepr`
        """
        model = NotFoundRepr()
        if include_optional:
            return NotFoundRepr(
                msg = '',
                description = None,
                code = '',
                cause = None,
                error_id = ''
            )
        else:
            return NotFoundRepr(
                msg = '',
                code = '',
        )
        """

    def testNotFoundRepr(self):
        """Test NotFoundRepr"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

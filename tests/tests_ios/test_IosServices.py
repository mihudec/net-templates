import unittest
from tests.tests_ios.BaseTemplateTestIos import BaseTemplateTestIos
from netcm.models.BaseModels.SharedModels import KeyBase
from netcm.models.services.vi.ServerModels import (
    TacacsServer,
    TacacsServerGroup,
    RadiusServer,
    RadiusServerGroup
)

class TestIosTacacsServer(BaseTemplateTestIos):

    TEMPLATE_NAME = 'ios_aaa_server_tacacs'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-01",
                "data": {
                    "params": TacacsServer(
                        name="TACACS-01",
                        server="1.2.3.4",
                        key=KeyBase(
                            encryption_type="0",
                            value="P@ssw0rd"
                        ),
                        single_connection=True
                    )
                },
                "result": (
                    "tacacs server TACACS-01\n"
                    " address ipv4 1.2.3.4\n"
                    " key 0 P@ssw0rd\n"
                    " single-connection\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)


class TestIosTacacsServerGroup(BaseTemplateTestIos):

    TEMPLATE_NAME = 'ios_aaa_group_tacacs'

    def test_01(self):
        test_cases = self.get_test_cases_from_resources()
        super().common_testbase(test_cases=test_cases)


class TestIosRadiusServerGroup(BaseTemplateTestIos):

    TEMPLATE_NAME = 'ios_aaa_group_radius'

    def test_01(self):
        test_cases = self.get_test_cases_from_resources()
        super().common_testbase(test_cases=test_cases)


class TestIosRadiusServer(BaseTemplateTestIos):

    TEMPLATE_NAME = 'ios_aaa_server_radius'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-01",
                "data": {
                    "params": RadiusServer(
                        name="RADIUS-01",
                        server="1.2.3.4",
                        key=KeyBase(
                            encryption_type="0",
                            value="P@ssw0rd"
                        ),
                        single_connection=True
                    )
                },
                "result": (
                    "radius server RADIUS-01\n"
                    " address ipv4 1.2.3.4\n"
                    " key 0 P@ssw0rd\n"
                    " single-connection\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)

if __name__ == '__main__':
    unittest.main()
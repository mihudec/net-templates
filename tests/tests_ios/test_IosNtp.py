import unittest
from tests.tests_ios.BaseTemplateTestIos import BaseTemplateTestIos
from net_models.models.services.vi.ServerModels import NtpKey, NtpServer, NtpConfig


class TestIosNtpAuthenticationKey(BaseTemplateTestIos):

    TEST_CLASS = NtpKey
    TEMPLATE_NAME = 'ios_ntp_authentication_key'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-01",
                "data": {
                    "params": NtpKey(
                        key_id=1,
                        encryption_type=0,
                        method="md5",
                        value="SuperSecret",
                        trusted=True
                    )
                },
                "result": (
                    "ntp authentication-key 1 md5 SuperSecret 0\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)


class TestIosNtpTrustedKey(BaseTemplateTestIos):

    TEST_CLASS = NtpKey
    TEMPLATE_NAME = 'ios_ntp_trusted_key'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-01",
                "data": {
                    "params": NtpKey(
                        key_id=1,
                        encryption_type=0,
                        method="md5",
                        value="SuperSecret",
                        trusted=True
                    )
                },
                "result": (
                    "ntp trusted-key 1\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)


class TestIosNtpKeys(BaseTemplateTestIos):

    TEST_CLASS = NtpKey
    TEMPLATE_NAME = 'ios_ntp_keys'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-01",
                "data": {
                    "params": [
                        NtpKey(
                            key_id=1,
                            encryption_type=0,
                            method="md5",
                            value="SuperSecret",
                            trusted=True
                        ),
                        NtpKey(
                            key_id=2,
                            encryption_type=0,
                            method="md5",
                            value="SuperSecret2",
                            trusted=True
                        ),
                        NtpKey(
                            key_id=3,
                            encryption_type=0,
                            method="md5",
                            value="SuperSecret3",
                            trusted=False
                        )
                    ]
                },
                "result": (
                    "ntp authentication-key 1 md5 SuperSecret 0\n"
                    "ntp authentication-key 2 md5 SuperSecret2 0\n"
                    "ntp authentication-key 3 md5 SuperSecret3 0\n"
                    "ntp trusted-key 1\n"
                    "ntp trusted-key 2\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)


class TestNtpSession(BaseTemplateTestIos):

    TEST_CLASS = NtpServer
    TEMPLATE_NAME = 'ios_ntp_session'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-Server-01",
                "data": {
                    "params": NtpServer(
                        server="192.0.2.1",
                        vrf="TEST-VRF",
                        prefer=True
                    ),
                    "session_type": "server"
                },
                "result": (
                    "ntp server vrf TEST-VRF 192.0.2.1 prefer\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)

del BaseTemplateTestIos

if __name__ == '__main__':
    unittest.main()
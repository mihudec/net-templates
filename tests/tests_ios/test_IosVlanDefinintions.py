import unittest

from net_models.models.BaseModels.SharedModels import VLANModel

from tests.tests_ios.BaseTemplateTestIos import BaseTemplateTestIos


class TestIosVrfDefinition(BaseTemplateTestIos):

    TEMPLATE_NAME = 'ios_vlan'
    TEST_CLASS = VLANModel

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-Single-Vlan",
                "data": {
                    "params": VLANModel(
                        vlan_id=10,
                        name="Vlan-10"
                    )
                },
                "result": (
                    "vlan 10\n"
                    " name Vlan-10\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)

class TestIosVLanDefinitions(BaseTemplateTestIos):

    TEMPLATE_NAME = 'ios_vlan_all'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-Multiple-Vlans",
                "data": {
                    "params": [
                        VLANModel(vlan_id=10, name="Vlan-10"),
                        VLANModel(vlan_id=20, name="Vlan-20")
                    ]
                },
                "result": (
                    "vlan 10\n"
                    " name Vlan-10\n"
                    "vlan 20\n"
                    " name Vlan-20\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)

del BaseTemplateTestIos

if __name__ == '__main__':
    unittest.main()
import unittest
from tests.tests_ios.BaseTemplateTestIos import BaseTemplateTestIos
from netcm.models.interfaces.vi import (
    InterfaceModel,
    InterfaceSwitchportModel
)

class TestIosInterfaceL2(BaseTemplateTestIos):

    TEMPLATE_NAME = "ios_interface_l2_port"

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-Model-Access-01",
                "data": {
                    "params": InterfaceSwitchportModel(
                        mode="access"
                    )
                },
                "result": (
                    " switchport mode access\n"
                )
            },
            {
                "test_name": "Test-Model-Access-02",
                "data": {
                    "params": InterfaceSwitchportModel(
                        mode="access",
                        untagged_vlan=10
                    )
                },
                "result": (
                    " switchport mode access\n"
                    " switchport access vlan 10\n"
                )
            },
            {
                "test_name": "Test-Model-Trunk-01",
                "data": {
                    "params": InterfaceSwitchportModel(
                        mode="trunk",
                        untagged_vlan=10
                    )
                },
                "result": (
                    " switchport mode trunk\n"
                    " switchport trunk native vlan 10\n"
                )
            },
            {
                "test_name": "Test-Model-Trunk-02",
                "data": {
                    "params": InterfaceSwitchportModel(
                        mode="trunk",
                        encapsulation="dot1q",
                        untagged_vlan=10
                    )
                },
                "result": (
                    " switchport trunk encapsulation dot1q\n"
                    " switchport mode trunk\n"
                    " switchport trunk native vlan 10\n"
                )
            },
            {
                "test_name": "Test-Model-Trunk-03",
                "data": {
                    "params": InterfaceSwitchportModel(
                        mode="trunk",
                        encapsulation="dot1q",
                        untagged_vlan=10,
                        allowed_vlans=[20,21,22,30,31,32,40],
                        negotiation=False
                    )
                },
                "result": (
                    " switchport trunk encapsulation dot1q\n"
                    " switchport mode trunk\n"
                    " switchport trunk native vlan 10\n"
                    " switchport trunk allowed vlan 20-22,30-32,40\n"
                    " switchport nonegotiate\n"
                )
            },
            {
                "test_name": "Test-Model-Trunk-04-With-Defaults",
                "data": {
                    "params": InterfaceSwitchportModel(negotiation=True),
                    "INCLUDE_DEFAULTS": True
                },
                "result": (
                    " no switchport nonegotiate\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)

    def test_02(self):
        test_cases = self.get_test_cases_from_resources()
        super().common_testbase(test_cases=test_cases)


class TestIosInterfaceBase(BaseTemplateTestIos):

    TEMPLATE_NAME = "ios_interface_base"

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-Dict-01",
                "data": {
                    "interface": {
                        "name": "Vlan1",
                        "description": "Test"
                    }
                },
                "result": (
                    "interface Vlan1\n"
                    " description Test\n"
                )
            },
            {
                "test_name": "Test-Model-01",
                "data": {
                    "interface": InterfaceModel(name="Vlan1", description="Test")
                },
                "result": (
                    "interface Vlan1\n"
                    " description Test\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)



class TestIosInterfaceAll(BaseTemplateTestIos):

    TEMPLATE_NAME = "ios_interfaces"

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-01",
                "data": {
                    "interfaces": {
                        "Vlan1": {
                            "description": "Test"
                        },
                        "Vlan2": {
                            "description": "Test"
                        }
                    }
                },
                "result": (
                    "interface Vlan1\n"
                    " description Test\n"
                    "!\n"
                    "interface Vlan2\n"
                    " description Test\n"
                    "!\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)

del BaseTemplateTestIos

if __name__ == '__main__':
    unittest.main()
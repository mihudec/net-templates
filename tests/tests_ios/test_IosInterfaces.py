import unittest
from tests.tests_ios.BaseTemplateTestIos import BaseTemplateTestIos
from net_models.models.interfaces.vi import (
    InterfaceCdpConfig,
    InterfaceLldpConfig,
    InterfaceBfdConfig,
    InterfaceModel,
    InterfaceSwitchportModel
)

class TestIosInterfaceL2(BaseTemplateTestIos):

    TEST_CLASS = InterfaceSwitchportModel
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


class TestInterfaceDiscoveryCdp(BaseTemplateTestIos):

    TEST_CLASS = InterfaceCdpConfig
    TEMPLATE_NAME = 'ios_interface_discovery_cdp'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-Enabled-Platform-Default-On_INCLUDE_DEFAULTS-Off",
                "data": {
                    "params": {
                        "enabled": True
                    },
                    "PLATFORM_CDP_DEFAULT_ON": True,
                    "INCLUDE_DEFAULTS": False
                },
                "result": ""
            },
            {
                "test_name": "Test-Enabled-Platform-Default-On_INCLUDE_DEFAULTS-On",
                "data": {
                    "params": {
                        "enabled": True
                    },
                    "PLATFORM_CDP_DEFAULT_ON": True,
                    "INCLUDE_DEFAULTS": True
                },
                "result": (
                    " cdp enable\n"
                )
            },
            {
                "test_name": "Test-Disabled-Platform-Default-On_INCLUDE_DEFAULTS-Off",
                "data": {
                    "params": {
                        "enabled": False
                    },
                    "PLATFORM_CDP_DEFAULT_ON": True,
                    "INCLUDE_DEFAULTS": False
                },
                "result": (
                    " no cdp enable\n"
                )
            },
            {
                "test_name": "Test-Disabled-Platform-Default-On_INCLUDE_DEFAULTS-On",
                "data": {
                    "params": {
                        "enabled": False
                    },
                    "PLATFORM_CDP_DEFAULT_ON": True,
                    "INCLUDE_DEFAULTS": True
                },
                "result": (
                    " no cdp enable\n"
                )
            },
            {
                "test_name": "Test-Enabled-Platform-Default-Off_INCLUDE_DEFAULTS-Off",
                "data": {
                    "params": {
                        "enabled": True
                    },
                    "PLATFORM_CDP_DEFAULT_ON": False,
                    "INCLUDE_DEFAULTS": False
                },
                "result": (
                    " cdp enable\n"
                )
            },
            {
                "test_name": "Test-Enabled-Platform-Default-Off_INCLUDE_DEFAULTS-On",
                "data": {
                    "params": {
                        "enabled": True
                    },
                    "PLATFORM_CDP_DEFAULT_ON": False,
                    "INCLUDE_DEFAULTS": True
                },
                "result": (
                    " cdp enable\n"
                )
            },
            {
                "test_name": "Test-Disabled-Platform-Default-Off_INCLUDE_DEFAULTS-Off",
                "data": {
                    "params": {
                        "enabled": False
                    },
                    "PLATFORM_CDP_DEFAULT_ON": False,
                    "INCLUDE_DEFAULTS": False
                },
                "result": ""
            },
            {
                "test_name": "Test-Disabled-Platform-Default-Off_INCLUDE_DEFAULTS-On",
                "data": {
                    "params": {
                        "enabled": False
                    },
                    "PLATFORM_CDP_DEFAULT_ON": False,
                    "INCLUDE_DEFAULTS": True
                },
                "result": (
                    " no cdp enable\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)



class TestInterfaceDiscoveryLldp(BaseTemplateTestIos):

    TEST_CLASS = InterfaceLldpConfig
    TEMPLATE_NAME = 'ios_interface_discovery_lldp'

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test_Transmit-On_Receive-On_Defaults-Off",
                "data": {
                    "params": {
                        "transmit": True,
                        "receive": True
                    },
                    "INCLUDE_DEFAULTS": False
                },
                "result": ""
            },
            {
                "test_name": "Test_Transmit-On_Receive-On_Defaults-On",
                "data": {
                    "params": {
                        "transmit": True,
                        "receive": True
                    },
                    "INCLUDE_DEFAULTS": True
                },
                "result": (
                    " lldp transmit\n"
                    " lldp receive\n"
                )
            },
            {
                "test_name": "Test_Transmit-Off_Receive-Off_Defaults-Off",
                "data": {
                    "params": {
                        "transmit": False,
                        "receive": False
                    },
                    "INCLUDE_DEFAULTS": False
                },
                "result": (
                    " no lldp transmit\n"
                    " no lldp receive\n"
                )
            },
            {
                "test_name": "Test_Transmit-Off_Receive-Off_Defaults-On",
                "data": {
                    "params": {
                        "transmit": False,
                        "receive": False
                    },
                    "INCLUDE_DEFAULTS": True
                },
                "result": (
                    " no lldp transmit\n"
                    " no lldp receive\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)


class TestIosInterfaceBfd(BaseTemplateTestIos):

    TEST_CLASS = InterfaceBfdConfig
    TEMPLATE_NAME = "ios_interface_bfd"

    def test_01(self):
        test_cases = [
            {
                "test_name": "Test-Interface-BFD-Template-01",
                "data": {
                    "params": InterfaceBfdConfig(
                        template="BFD-Template-01"
                    )
                },
                "result": (
                    " bfd template BFD-Template-01\n"
                )
            }
        ]
        super().common_testbase(test_cases=test_cases)


class TestIosInterfaceBase(BaseTemplateTestIos):

    TEST_CLASS = InterfaceModel
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
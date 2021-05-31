import unittest
from filters import FilterModule, TemplateFilters


class TestTemplateFiltersBase(unittest.TestCase):

    pass

class TestToVlanRange(TestTemplateFiltersBase):

    def test_from_int_list(self):
        test_cases = [
            {
                "test_name": "Test-From-Int-01",
                "data": list(range(1,4)),
                "result": "1-3"
            },
            {
                "test_name": "Test-From-Int-02",
                "data": [1, 3, 5],
                "result": "1,3,5"
            },
            {
                "test_name": "Test-From-Int-03",
                "data": [1,2,3,4,5,7,8,9,11],
                "result": "1-5,7-9,11"
            },
            {
                "test_name": "Test-From-Text-01",
                "data": "all",
                "result": "all"
            },
            {
                "test_name": "Test-From-Text-02",
                "data": "none",
                "result": "none"
            }
        ]
        for test_case in test_cases:
            with self.subTest(msg=test_case["test_name"]):
                want = test_case["result"]
                have = TemplateFilters.to_vlan_range(test_case["data"])
                self.assertEqual(want, have)


class TestValidateData(TestTemplateFiltersBase):

    TEST_CLASS = FilterModule

    def test_01(self):
        filter_object = self.TEST_CLASS()
        test_data = {
            "name": "Test",
            "server": "192.0.2.1",
            "timeout": 10
        }
        self.assertTrue(filter_object.validate_data(data=test_data, model="RadiusServer"))


del TestTemplateFiltersBase

if __name__ == '__main__':
    unittest.main()
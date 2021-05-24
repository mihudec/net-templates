import unittest
from filters import TemplateFilters


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



del TestTemplateFiltersBase

if __name__ == '__main__':
    unittest.main()
import unittest
from src.integrations.dynatrace import get_dynatrace_data

class TestDynatrace(unittest.TestCase):

    def test_get_dynatrace_data(self):
        data = get_dynatrace_data()
        # Add assertions based on the expected data structure
        self.assertIsInstance(data, dict)
        self.assertIn('timeseriesId', data)

if __name__ == '__main__':
    unittest.main()

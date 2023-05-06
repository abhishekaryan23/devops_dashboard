import unittest
from src.integrations.confluence import get_confluence_data

class TestConfluence(unittest.TestCase):

    def test_get_confluence_data(self):
        data = get_confluence_data()
        # Add assertions based on the expected data structure
        self.assertIsInstance(data, dict)
        self.assertIn('results', data)

if __name__ == '__main__':
    unittest.main()

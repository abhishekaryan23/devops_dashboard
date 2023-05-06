import unittest
from src.integrations.jira import get_jira_data

class TestJira(unittest.TestCase):

    def test_get_jira_data(self):
        data = get_jira_data()
        # Add assertions based on the expected data structure
        self.assertIsInstance(data, dict)
        self.assertIn('issues', data)

if __name__ == '__main__':
    unittest.main()

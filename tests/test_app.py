import unittest
from crm_app.app import app  # Убедитесь, что путь правильный
from crm_app.auth.routes import main  # Убедитесь, что путь правильный

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()

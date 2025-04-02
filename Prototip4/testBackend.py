import unittest
from unittest.mock import patch
import requests

class TestBackendServices(unittest.TestCase):
    BASE_URL = "http://localhost:5000"  # Replace with your actual base URL

    @patch("requests.post")
    def test_login_valid_user(self, mock_post):
        # Mocking the response for a valid user login
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "id": 1,
            "username": "mare",
            "email": "prova@gmail.com",
            "token": "token12345",
            "idrole": "2",
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }
        
        # Define the endpoint and payload
        url = f"{self.BASE_URL}/login"
        payload = {"username": "mare", "password": "password123"}
        
        # Perform the POST request
        response = requests.post(url, json=payload)
        
        # Assertions to verify the response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["coderesponse"], "1")
        self.assertEqual(data["msg"], "Usuari Ok")
        self.assertEqual(data["username"], "mare")
        self.assertEqual(data["email"], "prova@gmail.com")
        self.assertEqual(data["token"], "token12345")

if __name__ == "__main__":
        unittest.main()
    
import unittest
from unittest.mock import patch
from clientP4 import DAOUser, DAOChild, DAOTap, User, Child, Tap, Error

# FILE: Prototip4/test_testBackend.py

class TestBackendServices(unittest.TestCase):
    BASE_URL = "http://localhost:5000"

    @patch("requests.post")
    def test_login_valid_user(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "id": 1,
            "username": "mare",
            "email": "prova@gmail.com",
            "token": "token12345",
            "idrole": "2",
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }
        dao_user = DAOUser()
        result = dao_user.login("mare", "password123")
        self.assertIsInstance(result, User)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.username, "mare")
        self.assertEqual(result.email, "prova@gmail.com")

    @patch("requests.post")
    def test_login_invalid_user(self, mock_post):
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {
            "coderesponse": "0",
            "msg": "No validat"
        }
        dao_user = DAOUser()
        result = dao_user.login("invalid_user", "wrong_password")
        self.assertIsInstance(result, Error)
        self.assertEqual(result.code, 400)
        self.assertEqual(result.description, "No validat")

    @patch("requests.get")
    def test_get_children_no_child(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []
        dao_child = DAOChild()
        result = dao_child.get_children_by_user_id(1)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    @patch("requests.get")
    def test_get_children_one_child(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "id": 1,
                "child_name": "Carol Child",
                "sleep_average": 8,
                "treatment_id": 1,
                "time": 6
            }
        ]
        dao_child = DAOChild()
        result = dao_child.get_children_by_user_id(2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Child)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].name, "Carol Child")

    @patch("requests.get")
    def test_get_taps_no_tap(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []
        dao_tap = DAOTap()
        result = dao_tap.get_taps_by_child_id(1)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    @patch("requests.get")
    def test_get_taps_one_tap(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "id": 1,
                "child_id": 1,
                "status_id": 1,
                "user_id": 1,
                "init": "2024-12-18T19:42:43",
                "end": "2024-12-18T20:42:43"
            }
        ]
        dao_tap = DAOTap()
        result = dao_tap.get_taps_by_child_id(1)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Tap)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].child_id, 1)

if __name__ == "__main__":
    unittest.main()
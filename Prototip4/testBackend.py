import unittest
from unittest.mock import patch
import requests

class TestBackendServices(unittest.TestCase):
    BASE_URL = "http://localhost:5000"  # Replace with your actual base URL

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
        url = f"{self.BASE_URL}/login"
        payload = {"username": "mare", "password": "password123"}
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["coderesponse"], "1")
        self.assertEqual(data["msg"], "Usuari Ok")

    @patch("requests.post")
    def test_login_invalid_user(self, mock_post):
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {
            "coderesponse": "0",
            "msg": "No validat"
        }
        url = f"{self.BASE_URL}/login"
        payload = {"username": "invalid_user", "password": "wrong_password"}
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertEqual(data["coderesponse"], "0")
        self.assertEqual(data["msg"], "No validat")

    @patch("requests.get")
    def test_getchild_no_child(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "msg": "No Child",
            "coderesponse": "1",
            "children": []
        }
        url = f"{self.BASE_URL}/getchild/1"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["coderesponse"], "1")
        self.assertEqual(data["msg"], "No Child")
        self.assertEqual(data["children"], [])

    @patch("requests.get")
    def test_getchild_one_child(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "msg": "1",
            "coderesponse": "1",
            "children": [
                {
                    "id": 1,
                    "child_name": "Carol Child",
                    "sleep_average": 8,
                    "treatment_id": 1,
                    "time": 6
                }
            ]
        }
        url = f"{self.BASE_URL}/getchild/2"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["coderesponse"], "1")
        self.assertEqual(data["msg"], "1")
        self.assertEqual(len(data["children"]), 1)

    @patch("requests.get")
    def test_getchild_multiple_children(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "msg": "2",
            "coderesponse": "1",
            "children": [
                {
                    "id": 1,
                    "child_name": "Carol Child",
                    "sleep_average": 8,
                    "treatment_id": 1,
                    "time": 6
                },
                {
                    "id": 2,
                    "child_name": "Jaco Child",
                    "sleep_average": 10,
                    "treatment_id": 2,
                    "time": 6
                }
            ]
        }
        url = f"{self.BASE_URL}/getchild/3"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["coderesponse"], "1")
        self.assertEqual(data["msg"], "2")
        self.assertGreater(len(data["children"]), 1)

if __name__ == "__main__":
        unittest.main()
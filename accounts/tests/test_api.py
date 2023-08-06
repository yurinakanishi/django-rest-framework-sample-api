from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import UserAccount


class BaseTestCase(APITestCase):
    def setUp(self):
        self.user = UserAccount.objects.create_user(
            name="test", email="testcase@example.com", password="testcase"
        )

    def test_login(self):
        data = {"email": "testcase@example.com", "password": "testcase"}
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.refresh_token = response.data["refresh"]
        self.access_token = response.data["access"]

    def set_auth_header(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")


class RegistrationTestCase:
    def test_registration(self):
        data = {
            "name": "test",
            "email": "testcase@example.com",
            "password": "t3est7ca3se",
        }
        self.test_login()
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LogoutTestCase(BaseTestCase):
    def test_logout(self):
        self.test_login()
        self.set_auth_header(self.access_token)
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)


class GetUserInfoTestCase(BaseTestCase):
    def test_get_user_info(self):
        self.test_login()
        self.set_auth_header(self.access_token)
        response = self.client.get(reverse("user"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "test")
        self.assertEqual(response.data["email"], "testcase@example.com")


class TokenVerifyTestCase(BaseTestCase):
    def test_token_verify(self):
        self.test_login()
        response = self.client.post(
            reverse("token_verify"), {"token": self.access_token}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(reverse("token_verify"), {"token": "wrong_token"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TokenRefreshTestCase(BaseTestCase):
    def test_token_refresh(self):
        self.test_login()
        response = self.client.post(
            reverse("token_refresh"), {"refresh": self.refresh_token}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(
            reverse("token_refresh"), {"refresh": "wrong_token"}
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

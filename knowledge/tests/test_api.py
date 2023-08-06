from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import UserAccount
from general.models import Language, Tag, GenreForUrl, Article


class BaseTestCase(APITestCase):
    def setUp(self):
        for choice in Language.NAME_CHOICES:
            Language.objects.create(name=choice[0])

        for i, choice in enumerate(GenreForUrl.NAME_CHOICES):
            GenreForUrl.objects.create(
                name=choice[0], name_jp=GenreForUrl.NAME_JP_CHOICES[i][0]
            )

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


class GetKnowledgeListTestCase:
    def test_get_knowledge(self):
        response = self.client.get(reverse("knowledge-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(reverse("knowledge-list-all"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(reverse("knowledge-list-jp"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(reverse("knowledge-list-all-jp"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetKnowledgeDetailTestCase:
    def test_get_knowledge(self):
        response = self.client.get(
            reverse("knowledge-detail-retrieve", args=["a-color-of-cheddar-cheese"])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateAndGetKnowledgeTestCase(BaseTestCase):
    def test_create_knowledge(self):
        self.test_login()
        self.set_auth_header(self.access_token)
        data = {
            "article": {
                "references": "dfdfd",
                "content": "sdsdsds",
                "excerpt": "dfdf",
                "kicker": "dfd",
            },
            "genre_for_url": 1,
            "name": "aaa",
            "notesite_url": "https://www.google.com",
            "published_date": "2023-8-2",
            "slug": "aaa",
            "tags": [],
            "type": "knowledge",
            "language": 1,
        }
        # print(json.dumps(data))
        response = self.client.post(
            reverse("knowledge-create"),
            data,
            format="json",
        )
        # print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_knowledge(self):
        self.test_create_knowledge()
        response = self.client.get(reverse("knowledge-detail-retrieve", args=["aaa"]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateKnowledgeTestCase(CreateAndGetKnowledgeTestCase):
    def test_update_knowledge(self):
        self.test_create_knowledge()
        self.test_login()
        self.set_auth_header(self.access_token)
        data = {
            "article": {
                "references": "dfdfd",
                "content": "sdsdsds",
                "excerpt": "dfdf",
                "kicker": "dfd",
            },
            "genre_for_url": 1,
            "name": "aaa",
            "notesite_url": "https://www.google.com",
            "published_date": "2023-8-2",
            "slug": "sss",
            "tags": [],
            "type": "knowledge",
            "language": 1,
        }

        response = self.client.put(
            reverse("knowledge-detail-update", args=["aaa"]),
            data,
            format="json",
        )
        # print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_knowledge(self):
        self.test_update_knowledge()
        response = self.client.get(reverse("knowledge-detail-retrieve", args=["aaa"]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

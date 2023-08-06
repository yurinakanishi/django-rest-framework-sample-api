from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ..models import Knowledge, Article, Tag, GenreForUrl
from ..serializers import KnowledgeSerializerForCreateUpdate
from general.models import Language


class KnowledgeSerializerTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        # Create some sample data for testing
        self.tag1 = Tag.objects.create(name="tag1", slug="tag1")
        self.tag2 = Tag.objects.create(name="tag2", slug="tag2")
        self.language = Language.objects.create(name="en")
        self.article_instance = Article.objects.create(
            references="dfdfd", content="sdsdsds", excerpt="dfdf", kicker="dfd"
        )

        self.genre_for_url = GenreForUrl.objects.create(name="knowledge", name_jp="知識")

        self.knowledge_data = {
            "name": "Test Knowledge",
            "slug": "test-knowledge",
            "notesite_url": "https://www.google.com",
            "type": "knowledge",
            "language": 1,
            "article": {
                "references": "dfdfd",
                "content": "sdsdsds",
                "excerpt": "dfdf",
                "kicker": "dfd",
            },
            "tags": [1, 2],
            "genre_for_url": 1,
        }

    def test_knowledge_serializer_create(self):
        serializer = KnowledgeSerializerForCreateUpdate(data=self.knowledge_data)
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())

        knowledge_instance = serializer.save()

        # Assert that the knowledge instance was saved correctly
        self.assertEqual(knowledge_instance.name, self.knowledge_data["name"])
        self.assertTrue(knowledge_instance.tags.filter(id=self.tag1.id).exists())
        self.assertTrue(knowledge_instance.tags.filter(id=self.tag2.id).exists())
        self.assertEqual(knowledge_instance.genre_for_url, self.genre_for_url)
        self.assertEqual(knowledge_instance.language, self.language)
        self.assertEqual(
            knowledge_instance.notesite_url, self.knowledge_data["notesite_url"]
        )
        self.assertEqual(knowledge_instance.slug, self.knowledge_data["slug"])
        self.assertEqual(knowledge_instance.type, self.knowledge_data["type"])

        # Assert that the related article instance was saved correctly
        article_instance = Article.objects.get(knowledge_article=knowledge_instance)
        self.assertEqual(
            article_instance.kicker, self.knowledge_data["article"]["kicker"]
        )
        self.assertEqual(
            article_instance.content, self.knowledge_data["article"]["content"]
        )
        self.assertEqual(
            article_instance.references, self.knowledge_data["article"]["references"]
        )
        self.assertEqual(
            article_instance.excerpt, self.knowledge_data["article"]["excerpt"]
        )

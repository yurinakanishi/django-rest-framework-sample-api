from django.test import TestCase
from knowledge.models import Knowledge
from general.models import Language, GenreForUrl, Article


class PostModelTests(TestCase):
    def setUp(self):
        self.language_instance = Language.objects.create(name="en")
        self.genre_for_url_instance = GenreForUrl.objects.create(
            name="knowledge", name_jp="知識"
        )

        self.article_instance = Article.objects.create(
            references="dfdfd", content="sdsdsds", excerpt="dfdf", kicker="dfd"
        )

    def test_is_empty(self):
        """Confirm that the database is empty."""
        saved_posts = Knowledge.objects.all()
        self.assertEqual(saved_posts.count(), 0)

    def test_is_count_one(self):
        """Confirm that the database is count one."""
        knowledge_instance = Knowledge.objects.create(
            article=self.article_instance,
            genre_for_url=self.genre_for_url_instance,
            name="aaa",
            notesite_url="https://www.google.com",
            slug="sss",
            type="knowledge",
            language=self.language_instance,
        )
        knowledge_instance.tags.set([])
        saved_posts = Knowledge.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    def test_saving_and_retrieving_posts(self):
        """Confirm that after saving, the data is retrieved correctly."""
        knowledge_instance = Knowledge.objects.create(
            article=self.article_instance,
            genre_for_url=self.genre_for_url_instance,
            name="aaa",
            notesite_url="https://www.google.com",
            slug="sss",
            type="knowledge",
            language=self.language_instance,
        )
        knowledge_instance.tags.set([])
        saved_posts = Knowledge.objects.all()
        actual_post = saved_posts[0]

        self.assertEqual(actual_post.name, "aaa")
        self.assertEqual(actual_post.slug, "sss")

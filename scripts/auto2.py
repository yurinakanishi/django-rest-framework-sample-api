from knowledge.models import Knowledge
from general.models import Language, Tag, GenreForURL, Article
from arts.models import Art, Artist, Museum, PaintingMethod, PaintingStyle, ArtsPeriod
from living_things.models import LivingThings, Habitat, Species
from foods.models import Food, CookingMethod, Ingredient
from django.db import connection
from django.contrib.auth.models import User
import json
from accounts.models import UserAccount
from locations.models import Country, Location
from movies.models import Movie, MovieRating


def run():
    # with open("auto_knowledge.json") as ff:
    #     knowledge_data = json.load(ff)

    # with open("auto_blogs.json") as ff:
    #     blogs_data = json.load(ff)

    # with open("auto_countries.json") as ff:
    #     countries_data = json.load(ff)

    with open("auto_movies.json") as ff:
        movies_data = json.load(ff)

    # prefetch common objects
    author = UserAccount.objects.get(pk=1)
    # genre_for_url_for_knowledge = GenreForURL.objects.get(name="knowledge")
    # genre_for_url_for_blogs = GenreForURL.objects.get(name="knowledge")
    # genre_for_url_for_countries = GenreForURL.objects.get(name="countries")
    # genre_for_url_for_movies = GenreForURL.objects.get(name="movies")
    # language_en = Language.objects.get(pk=1)
    # language_jp = Language.objects.get(pk=2)

    # articles_for_movies_list = []
    # rating_for_movies_list = []
    # movies_list = []

    # for a in reversed(movies_data):
    #     if a.get("language") == "en":
    #         language = language_en
    #         name = a.get("name")
    #     else:
    #         language = language_jp
    #         name = a.get("name", "") + " Jp"

    #     articles_for_movies_list.append(
    #         Article(
    #             content=a.get("content"),
    #             kicker=a.get("name"),
    #             excerpt=a.get("name"),
    #         )
    #     )

    #     rating_for_movies_list.append(
    #         MovieRating(
    #             story=a.get("story"),
    #             social_effect=a.get("social_effect"),
    #             business_successful=a.get("business_successful"),
    #             innovative=a.get("innovative"),
    #             music=a.get("music"),
    #             images=a.get("images"),
    #             rating_average=(
    #                 a.get("story")
    #                 + a.get("social_effect")
    #                 + a.get("business_successful")
    #                 + a.get("innovative")
    #                 + a.get("music")
    #                 + a.get("images")
    #             )
    #             / 6,
    #         )
    #     )

    #     movies_list.append(
    #         Movie(
    #             name=name,
    #             slug=a.get("slug"),
    #             type="movie",
    #             author=author,
    #             genre_for_url=genre_for_url_for_movies,
    #             language=language,
    #             themoviedb_id=a.get("id"),
    #         )
    #     )

    # articles_for_movies_list = Article.objects.bulk_create(articles_for_movies_list)
    # for movie in movies_list:
    #     print(movie.name)

    # rating_for_movies_list = MovieRating.objects.bulk_create(rating_for_movies_list)

    # for article, movie in zip(articles_for_movies_list, movies_list):
    #     movie.article = article

    # for rating, movie in zip(rating_for_movies_list, movies_list):
    #     movie.movie_rating = rating

    # Movie.objects.bulk_create(movies_list)

    # for a in reversed(knowledge_data):
    #     if a.get("language") == "en":
    #         language = language_en
    #     else:
    #         language = language_jp

    #     articles_for_knowledge_list.append(
    #         Article(
    #             content=a.get("content"),
    #             kicker=a.get("kicker"),
    #             excerpt=a.get("exerpt"),
    #         )
    #     )

    #     knowledge_list.append(
    #         Knowledge(
    #             name=a.get("name"),
    #             slug=a.get("slug"),
    #             type="knowledge",
    #             author=author,
    #             genre_for_url=genre_for_url_for_knowledge,
    #             language=language,
    #             notesite_url=a.get("notesite_url"),
    #         )
    #     )

    # for a in reversed(blogs_data):
    #     if a.get("language") == "en":
    #         language = language_en
    #     else:
    #         language = language_jp

    #     articles_for_blogs_list.append(
    #         Article(
    #             content=a.get("content"),
    #             kicker=a.get("kicker"),
    #             excerpt=a.get("exerpt"),
    #         )
    #     )

    #     blogs_list.append(
    #         Knowledge(
    #             name=a.get("name"),
    #             slug=a.get("slug"),
    #             type="blog",
    #             author=author,
    #             genre_for_url=genre_for_url_for_blogs,
    #             language=language,
    #             notesite_url=a.get("notesite_url"),
    #         )
    #     )

    # for a in reversed(countries_data):
    #     if a.get("language") == "en":
    #         language = language_en
    #     else:
    #         language = language_jp

    #     articles_for_countries_list.append(
    #         Article(
    #             content=a.get("content"),
    #             kicker=a.get("kicker"),
    #             excerpt=a.get("exerpt"),
    #         )
    #     )

    #     countries_list.append(
    #         Country(
    #             name=a.get("name"),
    #             slug=a.get("slug"),
    #             genre_for_url=genre_for_url_for_countries,
    #             language=language,
    #         )
    #     )

    # articles_for_knowledge_list = Article.objects.bulk_create(
    #     articles_for_knowledge_list
    # )
    # articles_for_blogs_list = Article.objects.bulk_create(articles_for_blogs_list)
    # articles_for_countries_list = Article.objects.bulk_create(
    #     articles_for_countries_list
    # )

    # for article, knowledge in zip(articles_for_knowledge_list, knowledge_list):
    #     knowledge.article = article

    # for article, blog in zip(articles_for_blogs_list, blogs_list):
    #     blog.article = article

    # for article, country in zip(articles_for_countries_list, countries_list):
    #     country.article = article

    # Knowledge.objects.bulk_create(knowledge_list)
    # Knowledge.objects.bulk_create(blogs_list)
    # Country.objects.bulk_create(countries_list)

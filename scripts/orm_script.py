from knowledge.models import Knowledge
from django.db import connection
from django.contrib.auth.models import User


def run():
    # knowledge = Knowledge()
    # knowledge.name = "Django"
    # knowledge.slug = "django"
    # knowledge.name_jp = "ジャンゴ"
    # knowledge.type = "KNOWLEDGE"
    # knowledge.type_jp = "KNOWLEDGE"

    # knowledge.save()

    knowledge = Knowledge.objects.first()
    user = User.objects.first()
    print(knowledge)
    print(connection.queries)

from django.test import TestCase
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class vlozeni(TestCase):
    a = Article(title=f'article Title', author='admin', email='mujemail@seznam.cz')
    a.save()
    serializer = ArticleSerializer(a)
    serializer.data
    content = JSONRenderer().render(serializer.data)
    print(content)
    serializer = ArticleSerializer(Article.objects.all(), many=True)
    serializer.data
    content = JSONRenderer().render(serializer.data)
    print(content)
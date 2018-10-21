from rest_framework import viewsets
from DjangoWithVue.article.models import Article
from DjangoWithVue.article import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
from rest_framework import viewsets, permissions, pagination, response
from django_filters.rest_framework import DjangoFilterBackend

from wordindex.serializers import (
    WordIndexSerializer,
    WordSerializer,
    WordDetailSerializer,
    LargeIndexSetWordDetailSerializer
)
from wordindex.models import (
    STOP_WORD_DENSITY_THRESHOLD,
    STOP_WORD_ARTICLE_DENSITY_THRESHOLD,
    WordIndex, 
    Word,
    Webpage
)

from django.db.utils import IntegrityError
from django.db.models import Count, Sum
from django.shortcuts import redirect

from collections import OrderedDict

MAX_RESULT_SIZE = 100

class Pagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = MAX_RESULT_SIZE

class WordIndexViewset(viewsets.ModelViewSet):
    queryset = WordIndex.objects.all().order_by('-count')
    serializer_class = WordIndexSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "word__word",
        "url__url",
    ]


class WordViewset(viewsets.ModelViewSet):
    """
    To filter stopwords, use `WordDensityMax` and `ArticleDensityMax`. 
    Default values are `?WordDensityMax=0.0003&ArticleDensityMax=0.85`.
    To see all words, use `?WordDensityMax=1&ArticleDensityMax=1`.
    """
    queryset = Word.objects.all().order_by('-count')
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "word",
        "count",
        "isAlnum"
    ]
    lookup_field = 'word'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.wordindex_set.count() <= MAX_RESULT_SIZE:
            serializer = WordDetailSerializer(instance)
        else:
            serializer = LargeIndexSetWordDetailSerializer(instance)
        return response.Response(serializer.data)

    def get_queryset(self):
        queryset = self.queryset

        try:
            densityMax = float(self.request.GET.get('WordDensityMax', STOP_WORD_DENSITY_THRESHOLD))
            if densityMax < 1.0:
                densityMaxThreshold = Word.objects.filter(isAlnum=True).aggregate(count=(Sum('count')))['count'] * densityMax
                queryset = queryset.filter(count__lte=int(densityMaxThreshold))

        except ValueError:
            pass

        try:
            articleMax = float(self.request.GET.get('ArticleDensityMax', STOP_WORD_ARTICLE_DENSITY_THRESHOLD))
            if articleMax < 1.0:
                articleMaxThreshold = Webpage.objects.all().count() * articleMax
                queryset = queryset.annotate(
                    num_wordindex=Count('wordindex')
                ).filter(num_wordindex__lte=int(articleMaxThreshold))
        except ValueError:
            pass


        return queryset


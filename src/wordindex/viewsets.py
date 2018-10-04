from rest_framework import viewsets, permissions, pagination
from wordindex.serializers import WordIndexSerializer
from wordindex.models import WordIndex

from django.db.utils import IntegrityError
from django.shortcuts import redirect

class Pagination(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 1000

class WordIndexViewset(viewsets.ModelViewSet):
    queryset = WordIndex.objects.all()
    serializer_class = WordIndexSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Pagination
    search_fields = [
        "word",
        "url",
        "isStopWord",
    ]

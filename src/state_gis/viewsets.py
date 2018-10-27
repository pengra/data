from rest_framework import viewsets, permissions, pagination, response
from django_filters.rest_framework import DjangoFilterBackend

from state_gis.serializers import StateSerializer
from state_gis.models import State


class StateViewset(viewsets.ModelViewSet):
    """
    The zip files containing a bunch of GIS files.
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "code",
    ]
    lookup_field = 'code'

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(*args, **kwargs)
        return response.Response({
            "geoJson": "Some day...",
            **serializer
        })
        



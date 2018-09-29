from rest_framework import viewsets, permissions, pagination
from compas.models import Assessment
from compas.serializers import AssessmentSerializers

class Pagination(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 1000

class AssessmentViewset(viewsets.ModelViewSet):
    """
    If you'd like more details on the inmates (like name, address, etc) email me @ nortonjp@uw.edu.
    Also, these values were true as of 2015. These might not be true as of today.
    """
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Pagination
    lookup_field = 'assessment_id'
    search_fields = [
        'date',
        'case_id',
        'assessment_id',
        'violence_score',
        'recidivism_score',
        'fail_to_appear_score',
    ]
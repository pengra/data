from rest_framework import viewsets, permissions, pagination
from compas.models import Assessment
from compas.serializers import AssessmentSerializers


class AssessmentViewset(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination
    page_size = 100
    lookup_field = 'assessment_id'
    search_fields = [
        'date',
        'case_id',
        'assessment_id',
        'violence_score',
        'recidivism_score',
        'fail_to_appear_score',
    ]
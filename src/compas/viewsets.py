from rest_framework import viewsets, permissions
from compas.models import Assessment
from compas.serializers import AssessmentSerializers
from django_filters import rest_framework as filters


class AssessmentViewset(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'assessment_id'
    search_fields = [
        'date',
        'case_id',
        'assessment_id',
        'violence_score',
        'recidivism_score',
        'fail_to_appear_score',
    ]
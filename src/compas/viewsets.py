from rest_framework import viewsets, permissions, pagination, response
from django_filters.rest_framework import DjangoFilterBackend

from compas.models import Assessment
from compas.serializers import AssessmentSerializers

from collections import OrderedDict

class Pagination(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 1000

    def get_paginated_response(self, data, queryset):
        # import pdb; pdb.set_trace()
        return response.Response(OrderedDict([
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('meta', {
                'count': self.page.paginator.count,
                'sex': {
                    'males': queryset.filter(inmate__sex='male').count(),
                    'females': queryset.filter(inmate__sex='female').count(),
                },
                'ethnicity': {
                    'african-americans': queryset.filter(inmate__ethnicity='african-american').count(),
                    'native-americans': queryset.filter(inmate__ethnicity='native-american').count(),
                    'asians': queryset.filter(inmate__ethnicity='asian').count(),
                    'hispanics': queryset.filter(inmate__ethnicity='hispanic').count(),
                    'caucasians': queryset.filter(inmate__ethnicity='caucasian').count(),
                    'other': queryset.filter(inmate__ethnicity='other').count(),
                },
                'language': {
                    'english': queryset.filter(inmate__language='english').count(),
                    'spanish': queryset.filter(inmate__language='spanish').count()
                },
                'scores': {
                    'violence': {
                        None: queryset.filter(violence_score=None).count(),
                        1: queryset.filter(violence_score=1).count(),
                        2: queryset.filter(violence_score=2).count(),
                        3: queryset.filter(violence_score=3).count(),
                        4: queryset.filter(violence_score=4).count(),
                        5: queryset.filter(violence_score=5).count(),
                        6: queryset.filter(violence_score=6).count(),
                        7: queryset.filter(violence_score=7).count(),
                        8: queryset.filter(violence_score=8).count(),
                        9: queryset.filter(violence_score=9).count(),
                        10: queryset.filter(violence_score=10).count(),
                    },
                    'recidivism': {
                        None: queryset.filter(recidivism_score=None).count(),
                        1: queryset.filter(recidivism_score=1).count(),
                        2: queryset.filter(recidivism_score=2).count(),
                        3: queryset.filter(recidivism_score=3).count(),
                        4: queryset.filter(recidivism_score=4).count(),
                        5: queryset.filter(recidivism_score=5).count(),
                        6: queryset.filter(recidivism_score=6).count(),
                        7: queryset.filter(recidivism_score=7).count(),
                        8: queryset.filter(recidivism_score=8).count(),
                        9: queryset.filter(recidivism_score=9).count(),
                        10: queryset.filter(recidivism_score=10).count(),
                    },
                    'fail_to_appear': {
                        None: queryset.filter(fail_to_appear_score=None).count(),
                        1: queryset.filter(fail_to_appear_score=1).count(),
                        2: queryset.filter(fail_to_appear_score=2).count(),
                        3: queryset.filter(fail_to_appear_score=3).count(),
                        4: queryset.filter(fail_to_appear_score=4).count(),
                        5: queryset.filter(fail_to_appear_score=5).count(),
                        6: queryset.filter(fail_to_appear_score=6).count(),
                        7: queryset.filter(fail_to_appear_score=7).count(),
                        8: queryset.filter(fail_to_appear_score=8).count(),
                        9: queryset.filter(fail_to_appear_score=9).count(),
                        10: queryset.filter(fail_to_appear_score=10).count(),
                    },
                }
            }),
            ('results', data),
        ]))

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
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        'date',
        'inmate__ethnicity',
        'inmate__sex',
        'violence_score',
        'recidivism_score',
        'fail_to_appear_score',
        'inmate__language',
        'type',
    ]
    
    def get_paginated_response(self, data, queryset):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data, queryset)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data, queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
from rest_framework import routers
from geoip.viewsets import IPInfoViewset
from wikibags.viewsets import WikiArticleViewset
from compas.viewsets import AssessmentViewset

router = routers.DefaultRouter()

router.register('geoip', IPInfoViewset)
router.register('wikibags', WikiArticleViewset)
router.register('compas', AssessmentViewset)

urlpatterns = router.urls
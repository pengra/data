from rest_framework import routers
from geoip.viewsets import IPInfoViewset
from wikibags.viewsets import WikiArticleViewset
from compas.viewsets import AssessmentViewset
from wordindex.viewsets import WordViewset
from state_gis.viewsets import StateViewset

router = routers.DefaultRouter()

router.register('geoip', IPInfoViewset)
router.register('wikibags', WikiArticleViewset)
router.register('compas', AssessmentViewset)
router.register('wordindex', WordViewset)
router.register('state_gis', StateViewset)

urlpatterns = router.urls
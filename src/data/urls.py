from rest_framework import routers
from geoip.viewsets import IPInfoViewset
from wikibags.viewsets import WikiArticleViewset

router = routers.DefaultRouter()

router.register('geoip', IPInfoViewset)
router.register('wikibags', WikiArticleViewset)

urlpatterns = router.urls
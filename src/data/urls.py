from rest_framework import routers
from geoip.viewsets import IPInfoViewset

router = routers.DefaultRouter()

router.register('geoip', IPInfoViewset)

urlpatterns = router.urls
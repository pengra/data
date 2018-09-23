from rest_framework import viewsets, permissions, response
from geoip.serializers import IPInfoSerializer
from geoip.models import IPInfo
from geoip.tasks import get_or_create_ip

class IPInfoViewset(viewsets.ModelViewSet):
    queryset = IPInfo.objects.all()
    serializer_class = IPInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    lookup_field = 'IP'
    lookup_value_regex = r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'

    def list(self, request):
        data = {"help": [
            "Look up an IP with https://data.pengra.io/geoip/{IP_ADDR}/",
            "Check out the docs @ https://pengra.github.io/data/geoip"
        ]}
        return response.Response(data=data, status=404)

    def retrieve(self, request, IP=None):
        "Grab IPInfo if it doesn't exist."
        try:
            ip = get_or_create_ip(IP)
        except ValueError:
            return response.Response(data="Bad IP address", status=404)

        serializer = self.serializer_class(ip)
        return response.Response(serializer.data)
        
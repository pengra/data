from rest_framework import serializers
from geoip.models import IPInfo

class IPInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPInfo
        lookup_field = 'IP'
        fields = [
            'IP',
            'continent',
            'country',
            'region_code',
            'region_name',
            'city',
            'zip',
            'latitude',
            'longitude',
            'language',
        ]
        
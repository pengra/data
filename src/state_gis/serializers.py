from rest_framework import serializers
from state_gis.models import State


class StateSerializer(serializers.ModelSerializer):
    block_size = serializers.IntegerField(read_only=True)
    county_size = serializers.IntegerField(read_only=True)
    precinct_size = serializers.IntegerField(read_only=True)
    class Meta:
        model = State
        fields = [
            "code",
            "block_gis",
            "block_size",
            "block_count",
            "county_gis",
            "county_size",
            "county_count",
            "precinct_gis",
            "precinct_size",
            "precinct_count",
        ]
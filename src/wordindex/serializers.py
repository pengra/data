from rest_framework import serializers
from wordindex.models import WordIndex

class WordIndexSerializer(serializers.ModelSerializer):
    wordPercentage = serializers.FloatField(read_only=True)
    articleAppearancePercentage = serializers.FloatField(read_only=True)
    isStopWord = serializers.BooleanField(read_only=True)
    class Meta:
        model = WordIndex
        fields = [
            'updated_at',
            'url',
            'word',
            'count',
            'wordPercentage',
            'articleAppearancePercentage',
            'isStopWord',
        ]
        
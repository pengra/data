from rest_framework import serializers
from wordindex.models import WordIndex, Word


class WordIndexSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="url.url")
    class Meta:
        model = WordIndex
        fields = [
            'url',
            'count',
        ]


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = [
            'word',
            'count',
            'isAlnum',
        ]

class WordDetailSerializer(WordSerializer):
    indexes = WordIndexSerializer(source="wordindex_set", many=True, read_only=True)
    wordDensity = serializers.FloatField(read_only=True)
    articleDensity = serializers.FloatField(read_only=True)
    isStopWord = serializers.BooleanField(read_only=True)

    class Meta:
        model = Word
        fields = [
            'word',
            'count',
            'isAlnum',
            'wordDensity',
            'isStopWord',
            'articleDensity',
            'indexes',
        ]

class LargeIndexSetWordDetailSerializer(WordDetailSerializer):
    indexes = None
    class Meta:
        model = Word
        fields = [
            'word',
            'count',
            'isAlnum',
            'wordDensity',
            'isStopWord',
            'articleDensity',
        ]
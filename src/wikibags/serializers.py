from rest_framework import serializers
from wikibags.models import WikiArticle

class WikiArticleSerializer(serializers.ModelSerializer):
    bag = serializers.JSONField(source='sorted_bag')
    header_bag = serializers.JSONField(source='sorted_header_bag')
    class Meta:
        model = WikiArticle
        lookup_field = 'wiki_id'
        fields = [
            'updated_at',
            'wiki_id',
            'title',
            'header_bag_size',
            'bag_size',
            'header_bag',
            'bag',
        ]
        
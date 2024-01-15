from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'image', 'created_at', 'updated_at', 'author', 'author_username']

    def get_author_username(self, obj):
        return obj.get_author_username()

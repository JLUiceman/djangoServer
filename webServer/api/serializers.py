from rest_framework import serializers
from api.models import Article, Friend

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'article_type', 'article_title', 'article_author')

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'article_type', 'article_title', 'article_content', 'article_author')        

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'fullname', 'nickname')        
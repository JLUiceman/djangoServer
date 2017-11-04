from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from .models import Article, Friend
from . import views


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Article
		fields = ['article_title', 'article_content', 'article_type', 'pub_date']

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class FriendSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Friend
		fields = ('fullname', 'nickname')

class FriendViewSet(viewsets.ModelViewSet):
	queryset = Friend.objects.all()
	serializer_class = FriendSerializer
						
			
		


# router = routers.DefaultRouter()
# router.register(r'list', ArticleViewSet) 
# router.register(r'friend', FriendViewSet)    		
		

urlpatterns = [
    url(r'^article/$', views.article_list),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail),
]
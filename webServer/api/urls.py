from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from .models import Article, Friend
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Article
# 		fields = ['article_title', 'article_content', 'article_type', 'pub_date']

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class FriendSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Friend
# 		fields = ('fullname', 'nickname')

# class FriendViewSet(viewsets.ModelViewSet):
# 	queryset = Friend.objects.all()
# 	serializer_class = FriendSerializer
						
			
		


# router = routers.DefaultRouter()
# router.register(r'list', ArticleViewSet) 
# router.register(r'friend', FriendViewSet)    		
		

urlpatterns = [
    url(r'^isFriend/(?P<fullname>[0-9a-zA-Z_]+)$', views.FriendList.as_view()),
    url(r'^articles/list/$', views.ArticleList.as_view()),
    url(r'^article/detail/(?P<id>[0-9]+)/$', views.ArticleDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
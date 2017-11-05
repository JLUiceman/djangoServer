from .models import Article, Friend
from .serializers import ArticleSerializer, ArticleDetailSerializer, FriendSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    lookup_field = 'article_type'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # def get_queryset(self):
    #     return Article.objects.get(article_type = self.request.GET.get('type', 'javascript'))


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


class FriendList(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'fullname'
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
# class ArticleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     def get(self, request, *args, **kwarg):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class FriendList(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Friend.objects.get(pk=pk)
#         except Friend.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         friend = self.get_object(pk)
#         serializer = FriendSerializer(friend)
#         return Response(serializer.data)      


# @csrf_exempt
# def article_list(request, pk):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         article = Article.objects.all() 
#         serializer = ArticleSerializer(article, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def article_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """

#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)    
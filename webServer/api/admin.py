from django.contrib import admin

# Register your models here.

from .models import Article, Friend

admin.site.register(Article)
admin.site.register(Friend)
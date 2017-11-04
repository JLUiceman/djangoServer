from django.db import models

# Create your models here.

class Article(models.Model):
	pub_date = models.DateTimeField('date published')
	article_type = models.CharField(max_length=20)
	article_title = models.CharField(max_length=200)
	article_content = models.TextField()
	article_author = models.CharField(max_length=20, default='caiyongbin')
	class Meta:
		ordering = ['pub_date']
	def __str__(self):
		return self.article_title


class Friend(models.Model):
	fullname = models.CharField(max_length=20)
	nickname = models.CharField(max_length=20)
	def __str__(self):
		return self.nickname

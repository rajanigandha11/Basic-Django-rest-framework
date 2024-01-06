from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)

class Comment(models.Model):
	
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


class Category(models.Model):
	name = models.CharField(max_length=255, default='python')
	title = models.CharField(max_length=200)
	body = models.TextField()
	author = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)


	class Meta:
		verbose_name_plural = 'categories'


		def __str__(self):
			return self.title


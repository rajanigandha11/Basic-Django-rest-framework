from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User
from .models import Comment
from .models import Category



class BlogSerializer(serializers.ModelSerializer):
	author=serializers.ReadOnlyField(source='author.username')
	comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model= Blog
		fields=['id','title','body', 'author', 'comments']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts','comments']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields=['id','title','body', 'author']

class CategorySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'author', 'posts']


       
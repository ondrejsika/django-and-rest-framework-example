from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Author, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )

class AuthorSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'created_by',
        )


class BookSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'author',
            'title',
            'created_by',
        )

class BookFullSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'author',
            'title',
            'created_by',
        )
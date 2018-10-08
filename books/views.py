from rest_framework import generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, BookFullSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class BookFullList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookFullSerializer


class BookFullDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookFullSerializer
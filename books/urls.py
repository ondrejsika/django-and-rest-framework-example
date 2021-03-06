from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('books-full/', views.BookFullList.as_view()),
    path('books-full/<int:pk>/', views.BookFullDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
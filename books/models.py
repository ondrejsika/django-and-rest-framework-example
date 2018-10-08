from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64)

    created_by = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    created_by = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s: %s' % (self.author.name, self.title)
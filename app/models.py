from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=220)
    img = models.ImageField(upload_to='img/', blank=True, null=True)
    discription = models.TextField()
    author = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class LibraryModel(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="libs")
    books_order = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
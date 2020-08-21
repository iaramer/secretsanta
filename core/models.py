from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.email

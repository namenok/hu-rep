from django.db import models


class HomeInfo(models.Model):
    text = models.CharField(max_length=200)
    img = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

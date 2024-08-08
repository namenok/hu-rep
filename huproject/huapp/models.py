from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return f'{self.text[:50]}...'


class Foto(models.Model):

    image = models.ImageField(upload_to='media')
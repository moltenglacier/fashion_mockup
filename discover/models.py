from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    blurb = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    thumbnail_url = models.CharField(max_length=200)
    details_url = models.CharField(max_length=200)
    def __str__(self):
        return self.title

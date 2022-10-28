from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey()
    title = models.CharField(max_length=100)
    content = models.TextField()
from distutils.command.upload import upload

from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    serving = models.IntegerField()
    serving_unit = models.CharField(max_length=65)
    preparation_step = models.TextField()
    preparation_step_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField (auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')

from django.contrib.contenttypes.models import ContentType
from django.db import models


class Favorite(models.Model):
    priority = models.PositiveSmallIntegerField()
    model_name = models.ForeignKey(to=ContentType, on_delete=models.CASCADE)

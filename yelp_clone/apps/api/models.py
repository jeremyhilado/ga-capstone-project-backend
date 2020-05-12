from django.db import models
from apps.authentication.models import User


class Business(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255)
    rating = models.FloatField()
    price = models.CharField(max_length=5)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

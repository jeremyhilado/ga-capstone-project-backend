from django.db import models
from apps.authentication.models import User


class Business(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255, blank=True)
    category = models.CharField(max_length=255)
    location_city = models.CharField(max_length=255)
    location_state = models.CharField(max_length=2)
    price = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Businesses"

    def __str__(self):
        return self.name


class Review(models.Model):
    business = models.ForeignKey(Business, related_name='business_review', on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.business.name + " - " + self.review

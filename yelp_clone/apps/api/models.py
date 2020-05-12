from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.authentication.models import User


class PageType(models.Model):
    page_type = models.CharField(max_length=255)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class Category(models.Model):
    page_type = models.ForeignKey(PageType, related_name='category_type', on_delete=models.CASCADE)
    alias = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Coordinate(models.Model):
    page_type = models.ForeignKey(PageType, related_name='coordinate_type', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.latitude + " / " + self.longitude


class Transaction(models.Model):
    page_type = models.ForeignKey(PageType, related_name='transaction_type', on_delete=models.CASCADE)
    transactions = ArrayField(models.CharField(max_length=255))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self


class Location(models.Model):
    page_type = models.ForeignKey(PageType, related_name='location_type', on_delete=models.CASCADE)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=3)
    state = models.CharField(max_length=2)
    display_address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self


class Attribute(models.Model):
    page_type = models.ForeignKey(PageType, related_name='attribute_type', on_delete=models.CASCADE)
    alias = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255)
    is_closed = models.BooleanField(default=False)
    url = models.URLField(max_length=255)
    review_count = models.IntegerField()
    rating = models.FloatField()
    price = models.CharField(max_length=5)
    phone = models.CharField(max_length=11)
    distance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

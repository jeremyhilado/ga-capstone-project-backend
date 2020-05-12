from django.contrib import admin
from apps.api.models import (
    PageType, Category, Coordinate,
    Transaction, Location, Attribute
)

# Register your models here.
admin.site.register(PageType)
admin.site.register(Category)
admin.site.register(Coordinate)
admin.site.register(Transaction)
admin.site.register(Location)
admin.site.register(Attribute)

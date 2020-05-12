from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from apps.api.views import BusinessViewSet

router = DefaultRouter()
router.register('businesses', BusinessViewSet, basename='businesses')

urlpatterns = router.urls

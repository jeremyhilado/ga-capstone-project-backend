from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from apps.api.views import TypeViewSet

router = DefaultRouter()
router.register('page_types', TypeViewSet, basename='page_types')

urlpatterns = router.urls

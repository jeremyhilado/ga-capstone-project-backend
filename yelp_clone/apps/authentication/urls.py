from django.conf.urls import url
from apps.authentication.views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    url(r'^user/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^user/login/$', LoginAPIView.as_view(), name='login'),
]


from rest_framework import generics, viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Business
from .serializers import BusinessSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Business.objects.all()
        return queryset

    serializer_class = BusinessSerializer

    def create(self, request):
        business = Business.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if business:
            msg = 'Business with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        business = Business.objects.get(pk=self.kwargs["pk"])
        if not request.user == business.owner:
            raise PermissionDenied("You do not have permission to delete this business")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        business = Business.objects.get(pk=self.kwargs["pk"])
        if not request.user == business.owner:
            raise PermissionDenied(
                "You do not have permission to edit this business"
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

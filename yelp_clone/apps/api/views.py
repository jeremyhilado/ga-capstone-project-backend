from rest_framework import generics, viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    PageType, Category, Coordinate, Transaction,
    Location, Attribute
)
from .serializers import (
    AttributesSerializer, LocationSerializer, TransactionSerializer,
    CoordinateSerializer, CategorySerializer,
    TypeSerializer
)


class TypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = PageType.objects.all()
        return queryset

    serializer_class = TypeSerializer

    def create(self, request):
        page_type = PageType.objects.filter(
            name=request.data.get('type'),
            owner=request.user
        )
        if type:
            msg = 'Type with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        page_type = PageType.objects.get(pk=self.kwargs["pk"])
        if not request.user == page_type.owner:
            raise PermissionDenied("You do have not have permission to delete this type")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        page_type = PageType.objects.get(pk=self.kwargs["pk"])
        if not request.user == page_type.owner:
            raise PermissionDenied(
                "You do not have permission to edit this type"
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

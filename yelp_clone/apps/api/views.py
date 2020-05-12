from rest_framework import generics, viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Business, Review
from .serializers import BusinessSerializer, ReviewSerializer


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


class PublicBusinesses(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Business.objects.all().fiter(is_public=True)
        return queryset

    serializer_class = BusinessSerializer


class PublicBusinessDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Business.objects.all().filter(is_public=True)
        return  queryset

    serializer_class = BusinessSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Review.objects.all()
        return queryset

    serializer_class = ReviewSerializer

    def create(self, request):
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        review = Review.objects.get(pk=self.kwargs["pk"])
        if not request.user == review.owner:
            raise PermissionDenied("You do not have permission to delete this album")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        review = Review.objects.get(pk=self.kwargs["pk"])
        if not request.user == review.owner:
            raise PermissionDenied(
                "You do not have permission to edit this review"
            )

    def perform_create(self, serializer):
        serializer.save(owner=serializer.request.user)


class PublicReviews(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Review.objects.all().filter(is_public=True)
        return queryset

    serializer_class = ReviewSerializer


class PublicReviewDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Review.objects.all().filter(is_publc=True)
        return queryset

    serializer_class = ReviewSerializer

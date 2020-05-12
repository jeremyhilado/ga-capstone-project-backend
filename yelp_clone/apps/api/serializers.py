from rest_framework import serializers
from apps.api.models import Business, Review


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'business', 'rating', 'review', 'created_at',
                  'updated_at', 'owner', 'is_public')


class BusinessSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reviews = ReviewSerializer(many=True, read_only=True, required=False, source='business_review')

    class Meta:
        model = Business
        fields = ('id', 'name', 'image_url', 'location_city', 'location_state', 'category', 'price',
                  'phone', 'reviews', 'created_at', 'updated_at', 'owner',
                  'is_public')

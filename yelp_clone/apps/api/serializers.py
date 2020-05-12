from rest_framework import serializers
from apps.api.models import (
    PageType, Category, Coordinate,
    Transaction, Location, Attribute
)


class AttributesSerializer(serializers.Model):
    owner = serializers.ReadOnlyField(source='owners.username')

    class Meta:
        model = Attribute
        fields = ('id', 'name', 'image_url', 'is_closed',
                  'url', 'review_count', 'rating',
                  'price', 'phone',
                  'distance', 'created_at', 'updated_at', 'owner',
                  'is_public')


class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Location
        fields = ('id', 'address1', 'address2', 'address3',
                  'city', 'zip_code', 'country', 'state', 'display_address',
                  'created_at', 'updated_at', 'owner', 'is_public')


class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Transaction
        fields = ('id', 'transactions', 'created_at', 'updated_at',
                  'owner', 'is_public')


class CoordinateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Coordinate
        fields = ('id', 'latitude', 'longitude', 'created_at',
                  'updated_at', 'owner', 'is_public')


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = ('id', 'alias', 'title', 'created_at', 'updated_at',
                  'owner')


class TypeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    categories = CategorySerializer(many=True, read_only=True, required=False, source='category_type')
    coordinates = CoordinateSerializer(many=True, read_only=True, required=False, source='coordinate_type')
    transactions = TransactionSerializer(many=True, read_only=True, required=False, source='transaction_type')
    locations = LocationSerializer(many=True, read_only=True, required=False, source='location_type')
    attributes = AttributesSerializer(many=True, read_only=True, required=False, source='attribute_type')

    class Meta:
        model = PageType
        fields = ('id', 'page_type', 'attributes', 'categories', 'coordinates', 'transactions',
                  'locations', 'created_at', 'updated_at', 'owner', 'is_public')

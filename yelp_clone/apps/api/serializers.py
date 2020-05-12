from rest_framework import serializers
from apps.api.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Business
        fields = ('id', 'name', 'image_url', 'rating', 'price',
                  'phone', 'created_at', 'updated_at', 'owner',
                  'is_public')

        def __str__(self):
            return self.name

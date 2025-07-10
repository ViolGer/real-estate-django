from rest_framework import serializers
from .models import Property, PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(source='propertyimage_set', many=True)

    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'price', 'location', 'area', 'images']


class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Property, Favorite
from .serializers import PropertyDetailSerializer
from django.shortcuts import get_object_or_404

class PropertyDetailAPI(APIView):
    def get(self, request, pk):
        property = get_object_or_404(Property, pk=pk)
        serializer = PropertyDetailSerializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ToggleFavoriteAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        property_obj = get_object_or_404(Property, pk=pk)
        favorite, created = Favorite.objects.get_or_create(user=request.user, property=property_obj)

        if not created:
            favorite.delete()
            return Response({'message': 'Removed from favorites'}, status=status.HTTP_200_OK)

        return Response({'message': 'Added to favorites'}, status=status.HTTP_201_CREATED)
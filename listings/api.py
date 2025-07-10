from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertyDetailSerializer
from django.shortcuts import get_object_or_404

class PropertyDetailAPI(APIView):
    def get(self, request, pk):
        property = get_object_or_404(Property, pk=pk)
        serializer = PropertyDetailSerializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)

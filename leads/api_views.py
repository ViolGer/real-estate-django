from rest_framework import generics
from .models import Lead
from .serializers import LeadSerializer
from rest_framework.permissions import IsAuthenticated

class LeadListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        # Показываем только лиды текущего пользователя
        return Lead.objects.filter(agent=self.request.user)

    def perform_create(self, serializer):
        # Автоматически присваиваем текущего пользователя как агента
        serializer.save(agent=self.request.user)

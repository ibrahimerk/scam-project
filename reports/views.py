from rest_framework import viewsets, permissions
from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Base queryset
        queryset = Report.objects.all()
        
        # If user is authenticated, only show their reports
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)
            
        return queryset.order_by('-date_reported')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
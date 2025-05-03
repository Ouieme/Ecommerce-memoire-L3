from rest_framework import  viewsets
from .models import Admin
from .serializers import ProfileAdminSerializer
from .serializers import AdminSerializer

class Adminsets(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = ProfileAdminSerializer

class getadmins(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer









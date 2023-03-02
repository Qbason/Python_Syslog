#rest api 
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#model
from .models import Log,Device 
from .serializers import DeviceSerializer,LogSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filterset_fields = ['device', 'content','datetime']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['device__ipaddress', 'content','datetime']

    def perform_create(self, serializer):
        
        return super().perform_create(serializer)





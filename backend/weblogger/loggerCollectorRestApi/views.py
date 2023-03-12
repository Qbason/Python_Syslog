#rest api 
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#model
from .models import Log,Device 
from .serializers import DeviceSerializer,LogSerializer
from datetime import datetime, timedelta
from datetime import datetime


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filterset_fields = ['device']
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):

        queryset = Log.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            try:
                dt = datetime.strptime(search,"%Y-%m-%d")
                return queryset.filter(datetime__date=dt)
            except Exception:
                return queryset
        return queryset



    def perform_create(self, serializer):
        
        return super().perform_create(serializer)
    
@api_view(['GET'])
def CleanOldLogs(request):
    """
    For deleting old data
    """

    old_logs = Log.objects.filter(
        datetime__lte=datetime.now()-timedelta(days=30)
    )
    return Response(old_logs.delete())







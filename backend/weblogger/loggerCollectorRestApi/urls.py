from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import LogViewSet, DeviceViewSet, CleanOldLogs

router = DefaultRouter()

router.register(
    r'log',
    LogViewSet
)
router.register(
    r'device',
    DeviceViewSet
)


urlpatterns = [
    
    path("api/",include(router.urls)),
    path("api/cleanoldlogs/",CleanOldLogs)


]

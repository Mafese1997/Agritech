from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter # type: ignore
from .views import SensorViewSet, CropDataViewSet, WeatherForecastViewSet

router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'cropdata', CropDataViewSet)
router.register(r'weather', WeatherForecastViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import serializers # type: ignore
from .models import Sensor, CropData, WeatherForecast

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class CropDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropData
        fields = '__all__'

class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = '__all__'

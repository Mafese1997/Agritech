from rest_framework import viewsets # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .models import Sensor, CropData, WeatherForecast
from .serializers import SensorSerializer, CropDataSerializer, WeatherForecastSerializer
import requests # type: ignore
from datetime import datetime

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CropDataViewSet(viewsets.ModelViewSet):
    queryset = CropData.objects.all()
    serializer_class = CropDataSerializer

class WeatherForecastViewSet(viewsets.ModelViewSet):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer

    def create(self, request, *args, **kwargs):
        location = request.data.get('location')
        api_key = '26e88e4f27e09401da3bd53bf9d647d8'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'location': location,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'weather_condition': data['weather'][0]['description'],
                'forecast_time': datetime.fromtimestamp(data['dt'])
            }
            serializer = self.get_serializer(data=weather_data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Could not fetch weather data"}, status=status.HTTP_400_BAD_REQUEST)
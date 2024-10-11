from django.db import models
from django.contrib.auth.models import User

class Sensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.sensor_type})"

class CropData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    def __str__(self):
        return f"{self.sensor.name} - {self.timestamp}"

class WeatherForecast(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    weather_condition = models.CharField(max_length=50)
    forecast_time = models.DateTimeField()

    def __str__(self):
        return f"Weather at {self.location} - {self.forecast_time}"

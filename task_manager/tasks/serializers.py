from geopy.geocoders import Nominatim
from rest_framework import serializers
from .models import CustomUser, Task
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'mobile_number', 'password', 'address', 'latitude', 'longitude')

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            mobile_number=validated_data['mobile_number'],
            address=validated_data['address'],
        )
        user.set_password(validated_data['password'])

        # Fetch latitude and longitude
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(validated_data['address'])
        if location:
            user.latitude = location.latitude
            user.longitude = location.longitude

        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

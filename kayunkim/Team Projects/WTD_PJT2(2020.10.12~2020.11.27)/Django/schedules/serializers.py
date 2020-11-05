from rest_framework import serializers
from .models import Schedule
from accounts.serializers import UserSerializer

class ScheduleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Schedule
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Schedule
        fields = '__all__'


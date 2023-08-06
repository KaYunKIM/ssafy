from rest_framework import serializers
from .models import Project, Member, Meeting
from accounts.serializers import UserSerializer

class ProjectListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Project
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Project
        fields = '__all__'

class MemberListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Member
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    project = ProjectSerializer(required=False)
    class Meta:
        model = Member
        fields = '__all__'

class MeetingListSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(required=False)
    class Meta:
        model = Meeting
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(required=False)
    class Meta:
        model = Meeting
        fields = '__all__'
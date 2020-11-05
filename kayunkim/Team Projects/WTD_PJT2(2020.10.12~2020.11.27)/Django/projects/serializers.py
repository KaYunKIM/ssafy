from rest_framework import serializers
from .models import Project, Member, Meeting, Task, Keyword
from accounts.serializers import UserSerializer

#project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

#member
class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    project = ProjectSerializer(required=False)
    class Meta:
        model = Member
        fields = '__all__'

class MemberListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    project = ProjectSerializer(required=False)
    class Meta:
        model = Member
        fields = '__all__'

#meeting
class MeetingSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(required=False)
    class Meta:
        model = Meeting
        fields = '__all__'

class MeetingListSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(required=False)
    class Meta:
        model = Meeting
        fields = '__all__'

#task
class TaskSerializer(serializers.ModelSerializer):
    meeting = MeetingSerializer(required=False)
    class Meta:
        model = Task
        fields = '__all__'

class TaskListSerializer(serializers.ModelSerializer):
    meeting = MeetingSerializer(required=False)
    class Meta:
        model = Task
        fields = '__all__'

# keyword
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        feilds = 'title'

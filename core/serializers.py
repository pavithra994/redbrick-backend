from rest_framework import serializers
from core import models


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Request
        fields = "__all__"


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobType
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = "__all__"


class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StaffMember
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"


class SiteDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteDiary
        fields = "__all__"



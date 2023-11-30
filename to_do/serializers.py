from rest_framework import serializers

from to_do.models import Task

class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задач"""
    class Meta:
        model = Task
        fields = '__all__'
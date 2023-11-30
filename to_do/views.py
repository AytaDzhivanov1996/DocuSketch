from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from to_do.models import Task
from to_do.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Вьюсет для CRUD-операций с настройками для фильтрации и сортировки"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('name', 'created_at')
    ordering_fields = '__all__'

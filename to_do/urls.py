from django.urls import include, path
from rest_framework import routers

from to_do.views import TaskViewSet

task_router = routers.SimpleRouter()
task_router.register('', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(task_router.urls))
]
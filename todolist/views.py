from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from todolist.models import Task
from todolist.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

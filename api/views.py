from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User, Client, Project
from .serializers import UserSerializer, ClientSerializer, ProjectSerializer


class ClientListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for creating and listing clients.
    """
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Client.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting clients.
    """
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Client.objects.all()


class ProjectCreateView(generics.CreateAPIView):
    """
    API endpoint for creating a new project for a client.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        client_id = self.kwargs.get('client_id')
        client = Client.objects.get(pk=client_id)
        serializer.save(client=client, created_by=self.request.user)


class ProjectListView(generics.ListAPIView):
    """
    API endpoint for retrieving a list of projects assigned to the logged-in user.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)
    

class ClientProjectsDetailView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving a client's info along with its projects.
    """
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Client.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        projects_serializer = ProjectSerializer(instance.project_set.all(), many=True)
        data = serializer.data
        data['projects'] = projects_serializer.data
        return Response(data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    

class UserListView(generics.ListAPIView):
    """
    API endpoint for listing users.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()
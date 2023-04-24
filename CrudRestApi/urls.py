"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import ClientListCreateView, ClientDetailView,ProjectCreateView,ProjectListView,ClientProjectsDetailView,UserListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('api/clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('api/clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('api/clients/<int:pk>/projects/', ClientProjectsDetailView.as_view(), name='client-projects-detail'),
    path('api/users/', UserListView.as_view(), name='user-list'),
]


from django.contrib import admin
from .models import User,Client,Project
# # Register your models here.
# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ['client_name','created_at','created_by']
# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['project_name','client','created_at','created_by','users']

# admin.site.register(User)
admin.site.register(Client)
admin.site.register(Project)
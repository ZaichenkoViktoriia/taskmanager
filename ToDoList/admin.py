from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ToDoList.models import Task, Tag, Manager


@admin.register(Manager)
class ManagerAdmin(UserAdmin):
    list_display = UserAdmin.list_display


admin.site.register(Task)
admin.site.register(Tag)

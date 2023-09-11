from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'q1']  # Specify the fields to display in the list view

admin.site.register(User, UserAdmin)

from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'q1','q2','q3','q4','q5','q6','q7']

admin.site.register(UserInfo, UserInfoAdmin)


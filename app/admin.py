from django.contrib import admin
from .models import UserModels





@admin.register(UserModels)
class UserAdmin(admin.ModelAdmin):
    list_displey = ('title','second_name','sex', 'avatar', 'mail' )

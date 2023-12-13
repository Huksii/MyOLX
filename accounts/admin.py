from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user__username', 'user__is_active', 'user__is_staff', 'user__is_superuser', 'user__date_joined']
    search_fields = ['user__username']
    
    def photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.photo.url}" width="100px" height="180px">')
        else:
            return 'Нет фото'
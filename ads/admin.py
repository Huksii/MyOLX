from django.contrib import admin
from .models import Category, Ads

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['main_category', 'created_at']
    # prepopulated_fields = {'title': ['title']}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 20
    
    
@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'category', 'price', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 20
    
fieldsets = [
        [None, {
            'fields': ['title', 'image', 'category']
        }],
        ['Детали объявления', {
            'fields': ['description', 'price', 'contact', 'address']
        }],
        ['Связь', {
            'fields': ['whatsapp', 'telegram', 'instagram']
        }],
        ['Пользователь', {
            'fields': ['user',]
        }],
        ['Время создания', {
            'fields': ['created_at',],
            'classes': ['collapse',],
        }],
    ]
readonly_fields = ['created_at',]
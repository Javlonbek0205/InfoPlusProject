from django.contrib import admin
from .models import News, Category, Contact


# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'publish_time', 'status')
    search_fields = ('title','body')
    list_filter = ('status','publish_time', 'category')
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time','status')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

from django.contrib import admin
from .models import News, Category, Contact, Comment


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
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

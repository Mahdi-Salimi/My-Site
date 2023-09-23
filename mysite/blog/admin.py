from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'created_date', 'status', 'published_date')
    list_filter = ('title',)
    ordering = ['-created_date']
    search_fields = ['title','content']
    

admin.site.register(Post,PostAdmin)
admin.site.register(Category)


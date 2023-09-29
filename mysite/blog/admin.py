from django.contrib import admin
from .models import Post, Category,Comment  

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'created_date', 'status', 'published_date')
    list_filter = ('title',)
    ordering = ['-created_date']
    search_fields = ['title','content']
    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('name','approved')
    search_fields = ['name','post']
    
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)


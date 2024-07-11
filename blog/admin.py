from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'updated')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created', 'updated')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created')
    search_fields = ('text',)
    list_filter = ('author', 'created')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
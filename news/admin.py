from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published')
    list_filter = ('author', 'status', 'published')
    search_fields = ('title', 'content')
    ordering = ['status', 'published']
    date_hierarchy = 'published'
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)


admin.site.register(Post, PostAdmin)

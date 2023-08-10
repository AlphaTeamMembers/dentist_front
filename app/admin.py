from django.contrib import admin
from .models import Blog, About, Contact, Comment, Profile,Category


class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_at',
        'author',
        'is_published',
    ]


class AboutAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_at',
        'is_published'
    ]


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'created_at',
        'is_solved'
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'created_at',
        'is_solved'
    ]


admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Profile)
admin.site.register(Category)

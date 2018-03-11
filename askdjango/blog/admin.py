from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'status' ,'content_size', 'created_at', 'updated_at']

    actions = ['make_draft', 'make_published']
    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') # Queryset.update
        self.message_user(request, "{}건의 포스팅을 Draft로 변경".format(updated_count)) # Django의 message framework 활용

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') # Queryset.update
        self.message_user(request, "{}건의 포스팅을 Published로 변경".format(updated_count)) # Django의 message framework 활용

    make_published.short_description = "포스팅의 상태를 published로 변경"

admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']

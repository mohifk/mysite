from django.contrib import admin

from blog.models import Post,category,Comment
from django_summernote.admin import SummernoteModelAdmin
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display= '-empty-'
    list_display=('title','author','count_views','status','login_require','publish_date')
    list_filter=('status','author')
    ordering=['-create_date']
    search_fields=['title','content']
    summernote_fields=('content')

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display= '-empty-'
    list_display=('name','post','approved','create_date')
    list_filter=('post','approved')
    search_fields=['name','post']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin) 
admin.site.register(category)
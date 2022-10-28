from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display= '-empty-'
    #fields=('title',)
    #exclude=('title',)
    list_display=('title','count_views','status','publish_date')
    list_filter=('status',)
    ordering=['-create_date']
    search_fields=['title','content']
    #summernote_fields=('content')

admin.site.register(Post,PostAdmin) 
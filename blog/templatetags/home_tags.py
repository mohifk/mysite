from django import template
from blog.models import Post, category
register = template.Library()

@register.inclusion_tag('website_temp/blog_lastpost.html')
def lastestposts(arg=6):
    posts=Post.objects.filter(status=1).order_by('-publish_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('website_temp/blog_lastpost_home.html')
def lastestpost(arg=6):
    posts=Post.objects.filter(status=1).order_by('-publish_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog_temp/blog-post-category.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}
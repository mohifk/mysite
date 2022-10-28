from blog.models import Post,Comment
from django.shortcuts import render,get_object_or_404

def blog_view(request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'blog_temp/blog-home.html',context)


def blog_single(request,pid):
    posts=Post.objects.filter(status=1) 
    post_=get_object_or_404(Post,pk=pid,status=True)
    post_.count_views+=1
    post_.save()
    context={'post':post_}   
    return render(request,'blog_temp/blog-single.html',context)

from blog.models import Post,Comment
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponseRedirect 
from blog.forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def blog_view(request,**kwargs):
    posts=Post.objects.filter(publish_date__lte=timezone.now(),status=1) 
    if kwargs.get('cat_name') !=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') !=None:
        posts=posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') !=None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
    posts= Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger :
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts':posts}                                  ## the means is evry where {%posts%} means posts
    return render(request,'blog_temp/blog-home.html',context)



def blog_single(request,pid):
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'OK Dude your Comment submit SUCCESS It will be displayed after confirmation')
        else:
            messages.add_message(request,messages.ERROR,'Sorry Dude your Comment dident submit')
    posts=Post.objects.filter(status=1) 
    post_=get_object_or_404(Post,pk=pid,status=True)
    if not post_.login_require:
        post_.count_views+=1
        post_.save()        
        comments=Comment.objects.filter(post=post_.id,approved=1)  
        form= CommentForm()      
        context={'post':post_,'comments':comments,'form':form}
        return render(request,'blog_temp/blog-single.html',context)
    elif not request.user.is_authenticated :
        return HttpResponseRedirect(reverse('accounts:login'))

    elif request.user.is_authenticated:
        post_.count_views+=1
        post_.save()   
     
        comments=Comment.objects.filter(post=post_.id,approved=1)  
        form= CommentForm()      
        context={'post':post_,'comments':comments,'form':form} 
    return render(request,'blog_temp/blog-single.html',context)


def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET' :
        if s:= request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request,'blog_temp/blog-home.html',context)

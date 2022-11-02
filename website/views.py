from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib import messages
from website.forms import ContactForm, NameForm
from django.shortcuts import redirect
from blog.models import Post,Comment

def Home_page_view(request,**kwargs):
    posts=Post.objects.filter(status=1) 
    if kwargs.get('cat_name') !=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name') !=None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
    context={'posts':posts}
    return render(request,'website_temp/index.html',context)

def about_view(request):
    return render(request ,'website_temp/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact=form.save(commit=False)
            Contact.name='unknown'
            Contact.save()
            
            messages.add_message(request,messages.SUCCESS,'OK Dude your tiket submit SUCCESS')
        else:
            messages.add_message(request,messages.ERROR,'Sorry Dude your tiket dident submit')
    form = ContactForm()
    return render(request,'website_temp/contact.html',{'form':form})


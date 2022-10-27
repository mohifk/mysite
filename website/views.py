from django.shortcuts import render

def Home_page_view(request):
    return render(request,'.\website_temp\index.html')

def about_view(request):
    return render(request ,'.\website_temp\\about.html')

def contact_view(request):
    return render(request,'.\website_temp\contact.html')
# Create your views here.

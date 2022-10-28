from django.shortcuts import render
from django.contrib import messages
from website.forms import ContactForm, NameForm

def Home_page_view(request):
    return render(request,'.\website_temp\index.html')

def about_view(request):
    return render(request ,'.\website_temp\\about.html')

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
    return render(request,'.\website_temp\contact.html',{'form':form})

    

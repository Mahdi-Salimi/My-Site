from django.shortcuts import render
from website.models import Contact
from website.forms import ContactForm, NewsletterForm
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            unknown_name = form.data.copy()
            unknown_name['name'] = 'unknown'
            form = ContactForm(unknown_name)
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'Your ticket didnt submitted successfully')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return  HttpResponseRedirect('/')


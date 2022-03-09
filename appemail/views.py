from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from appemail.forms import studentForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
    form=studentForm()
    return render (request,'home.html',{'form':form}) 

def stdform(request):
    form=studentForm()
    if request.method =='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
            subject='LEarNinG SoFtWaRe'
            message='Dear canadidate,we are pleased to offer you an intership at our company'
            recipient=form.cleaned_data.get('email')
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient])
            messages.success(request,'success1')
            return redirect('/')
    return render(request,'home.html',{'form':form}) 

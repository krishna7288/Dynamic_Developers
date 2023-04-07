from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import ContctForm,JobForm,DetailsForm
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ContctForm(request.POST)                
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            message = form.cleaned_data['message']
            
            send_mail(
                f'Hello {name}..!',
                f'we are reciving your details {name} your mail({mail}): thanks for this message {message}',
                'dynamidevelopers@gmail.com',
                [mail],
                fail_silently=False,
            )
            
            messages.success(request, 'Thanks for the text')
            return redirect('home')
    else:
        form = ContctForm()
    return render(request, 'home.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form2 = DetailsForm(request.POST)                
        if form2.is_valid():
            form2.save()
            messages.success(request,"Thanks for the Message..!")
            return redirect("contact")
            # Redirect to success page
    else:
        form2 = DetailsForm()
    return render(request, 'contact.html', {'form2': form2})


def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def jobs(request):
    if request.method == 'POST':
        form1 = JobForm(request.POST,request.FILES)                
        if form1.is_valid():
            form1.save()
            messages.success(request,"Upload successfully completed")
            return redirect("jobs")
            # Redirect to success page
    else:
        form1 = JobForm()
    return render(request, 'jobs.html', {'form1': form1}) 


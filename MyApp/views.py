from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import SiteRequestForm
from .models import SiteRequest

# Create your views here.
def home(request):
    images = ['sampic.JPG', 'marisite.JPG', 'WebExCode.JPG']
    return render(request, 'home.html', {'images': images})

def contact(request):
    return render(request, 'Contact.html')

def services(request):
    return render(request, 'services.html')

def sites(request):
    return render(request, 'sites.html')

def request(request):
    if request.method == "POST":
        form = SiteRequestForm(request.POST)
        if form.is_valid():
            site_request = form.save()  # Save the form to the database

            # Send confirmation email
            send_mail(
                subject="New Website Request",
                message=f"New request from {site_request.full_name}\n\nDetails:\n{site_request}",
                from_email="thesitexperts@gmail.com",
                recipient_list=["thesitexperts@gmail.com"],  # Change this to your email
                fail_silently=False,
            )

            messages.success(request, "Your request has been submitted successfully!")
            return redirect("success")  # Redirect to the same page after submission

    else:
        form = SiteRequestForm()  # Initialize form for GET requests

    return render(request, "request.html", {"form": form})  # Ensure form is always passed to the template

def types(request):
    return render(request, 'types.html')

def seo(request):
    return render(request, 'seo.html')

def hosting(request):
    return render(request, 'hosting.html')

def website(request):
    return render(request, 'website.html')

def success(request):
    return render(request, 'success.html')
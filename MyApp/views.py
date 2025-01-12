from django.shortcuts import render

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
    return render(request, 'request.html')

def types(request):
    return render(request, 'types.html')

def seo(request):
    return render(request, 'seo.html')

def hosting(request):
    return render(request, 'hosting.html')

def website(request):
    return render(request, 'website.html')
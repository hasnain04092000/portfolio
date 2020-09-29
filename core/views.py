from django.shortcuts import render
from .models import Services,ServicesTop, Project, Contact, Profile, Banner
# Create your views here.



def index(request):
    context = {
        'services': Services.objects.all(),
        'servicesTop': ServicesTop.objects.all(),
        'project': Project.objects.all(),
        'contact': Contact.objects.all(),
        'profile': Profile.objects.all(),
        'wall':Banner.objects.get(title='banner'),
    }
    return render(request, 'index.html', context)
from django.shortcuts import render, HttpResponse
from home.models import Diamond
# from home.models import diamond
# Create your views here

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is a services page")

def diamond(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        diamond = Diamond(name=name, email=email, password=password) 
        diamond.save()
        
    return render(request, 'diamond.html')
    # return HttpResponse("This is about page")



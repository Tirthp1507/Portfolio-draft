from django.shortcuts import HttpResponse, render
from home.models import Contact

# Create your views here.


def home(request):
    # return HttpResponse("This is my homepage (/)")
    return render(request,'home.html')

def about(request):
    # return HttpResponse("This is my about page (/about)")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse("This is my projects page (/projects)")
    return render(request,'projects.html')

def contact(request):
    if request.method == "POST":
        print("This is post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        print("The data has been stored in database")
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()

    return render(request,'contact.html')
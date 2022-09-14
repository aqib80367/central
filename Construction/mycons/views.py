from django.shortcuts import render, HttpResponse
from mycons.models import Contact

# Create your views here.
def index(request):
    return render(request, "indexx.html")

def about(request):
    return render(request, "aboutt.html")

def services(request):
    return render(request, "servicess.html")

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        number = request.POST.get('number')
        # address = request.POST.get('address')
        # address2 = request.POST.get('address2')
    
        zip = request.POST.get('zip')
        contact = Contact(email=email, number=number, zip=zip)
        contact.save()
    return render(request, "contactt.html")
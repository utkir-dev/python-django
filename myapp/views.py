from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Dostavka

# Create your views here.
def hello(request):
    return HttpResponse('Salom dumyo !')

def goodbye(request):
    return HttpResponse('Xayr !!!')

def get_products(request):
    products=Dostavka.objects.all
    context={
        'products':products
    }
    return render(request,"products.html",context)


def get_completed(request):
    products=Dostavka.objects.all().filter(status="tayyor bo'ldi")
    context={
        'products':products
    }
    return render(request,"completed.html",context)

def get_prepearing(request):
    products=Dostavka.objects.all().filter(status="tayyorlanyapti")
    context={
        'products':products
    }
    return render(request,"prepearing.html",context)
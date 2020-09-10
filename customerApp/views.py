from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def homepage(request):
    return render(request,'customerApp/home.html')

def customerNames(request):
    cst = Customer.objects.all()
    return render(request, "customerApp/customersNames.html", {"temp": cst})

def add_Cust(request):
    return render (request,"customerApp/addCustomer.html")

def addCustomer(request):
    n = request.POST.get('name')
    c = request.POST.get('city')
    a = request.POST.get('age')

    c = Customer(name=n, city=c, age=a)
    c.save()
    cst = Customer.objects.all()

    return render(request, "customerApp/customersNames.html",{"temp":cst})


def customerDetails(request,i):
    cst = Customer.objects.get(id = i)
    print(cst)
    print("____________1********************")
    return render(request,'customerApp/customerDetails.html',{'temp':cst})



def deleteCustomer(request,i):
    c1 = Customer.objects.get(id=i)
    c1.delete()
    cst = Customer.objects.all()
    return render(request, "customerApp/customersNames.html", {"temp": cst})



def movieNames(request):
    m = Movie.objects.all()
    print(m)
    return render(request, 'customerApp/MovieNames.html', {'temp': m})

def add_Movie(request):
    return render(request, "customerApp/addMovie.html")


def addMovie(request):
    n = request.POST.get('name')
    a = request.POST.get('avail')

    m1 = Movie(name = n , avail = a)
    m1.save()

    m = Movie.objects.all()
    return render(request, 'customerApp/MovieNames.html', {'temp': m})


def deleteMovie(request,i):
    m1 = Movie.objects.get(id=i)
    print(m1)
    m1.delete()
    m = Movie.objects.all()
    print(m)
    return render(request, 'customerApp/MovieNames.html', {'temp': m})



def availableMovies(request,n,i):
    ml = []
    for m in Movie.objects.all():
        print(m)
        if m.avail >= 1:
            ml.append(m)
    ml.append(i)
    return render(request, 'customerApp/movieForCustomer.html', {'temp': ml})


def rentMovie(request,c_id,m_id):

    movie_list = Movie.objects.all()
    cust_list = Customer.objects.all()

    for m in movie_list:
        if m.id == m_id:
            m.avail -= 1
            m.save()
    for c in cust_list:
        if c.id == c_id:
            c.movie = Movie.objects.get(id = m_id)
            c.save()
    cst = Customer.objects.get(id = c_id)
    print(cst)
    return render(request, 'customerApp/customerDetails.html', {'temp': cst})








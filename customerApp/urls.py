from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.customerNames),
    path('addcustomer',views.add_Cust),
    path("add_customer",views.addCustomer),
    path("customernames/<int:i>",views.customerDetails),
    path('movienames',views.movieNames),
    path('add_movie',views.add_Movie),
    path('addMovie',views.addMovie),
    path('delete_mov/<int:i>', views.deleteMovie),
    path('delete_cust/<int:i>',views.deleteCustomer),
    path('customernames/<str:n>/<int:i>',views.availableMovies),
    path('showAvailableMovies/rent/<int:c_id>/<int:m_id>',views.rentMovie),


]
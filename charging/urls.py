from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/',views.book_station,name='book'),
    path('bookings/',views.bookings,name='bookings'),
]
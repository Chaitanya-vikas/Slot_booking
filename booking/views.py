from django.shortcuts import render, redirect, get_object_or_404
from .models import Slot
from django.contrib import messages
from django.utils import timezone

from django.contrib.auth.models import User
from django.http import HttpResponse
def create_secret_admin(request):
    # Change 'admin' and 'SecurePassword123!' to whatever you want
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('chaitanyavikas', 'chaitanyavikas@gmail.com', 'Vikas@1234')
        return HttpResponse("✅ Success! Live superuser created. Go to /admin to log in.")
    
    return HttpResponse("Admin already exists. Go log in!")

def home(request):
    today = timezone.localdate() 
    #added 'date' to order_by so it sorts chronologically by day
    available_slots = Slot.objects.filter(
        is_booked=False, 
        date__gte=today 
    ).order_by('date', 'start_time')
    
    return render(request, 'booking/index.html', {'slots': available_slots})

def book_slot(request, slot_id):
    if request.method == 'POST':
        slot = get_object_or_404(Slot, id=slot_id)
        
        # Concurrency check: Ensure it wasn't booked by someone else right before this click
        if not slot.is_booked:
            slot.is_booked = True
            slot.customer_name = request.POST.get('customer_name', 'Guest')
            slot.save()
            messages.success(request, 'Slot booked successfully!')
        else:
            messages.error(request, 'Sorry, this slot was just booked by someone else.')
            
        return redirect('my_bookings')
    return redirect('home')

def my_bookings(request):
    booked_slots = Slot.objects.filter(is_booked=True).order_by('date', 'start_time')
    return render(request, 'booking/my_bookings.html', {'slots': booked_slots})
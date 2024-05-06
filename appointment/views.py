from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment 

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False) 
            appointment.pet_owner = request.user  # Assuming logged-in user
            appointment.save()
            return redirect('appointment_success')  # Replace with a success view
    else:
        form = AppointmentForm()
    return render(request, 'appointment/booking_form.html', {'form': form})

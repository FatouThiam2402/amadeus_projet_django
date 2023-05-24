from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
# from hotel.models import Doctor
from .models import Inscription


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        # context = {
        #     'doctors': Doctor.objects.all()
        # }
        return render(request, "inscription/index.html")

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')
        # if doctor_id:
        #     doctor = get_object_or_404(Doctor, id=doctor_id)

        if(name and phone and email and date and time):
            Appointment.objects.create(
                name=name, phone=phone, email=email, date=date, time=time, note=note)
            messages.success(request,'inscription Reussi')
        return redirect('inscription')

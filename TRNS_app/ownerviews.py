from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render

from TRNS_app.forms import VehicleForm
from TRNS_app.models import Vehicles, Owner, BookVehicle, Payments


def vehicle_add(request):
    user = request.user
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                owner, created = Owner.objects.get_or_create(user=user)  # Get or create Owner instance
                data = form.save(commit=False)
                data.owner_name = owner  # Assign the Owner instance to the owner_name field
                data.save()
                return redirect('vehicle_view_ow')
            except IntegrityError:
                # Handle integrity error, maybe log it or show a meaningful message to the user
                pass
    return render(request, 'vehicle_add.html', {'form': form})

def vehicle_view_ow(request):
    u= Owner.objects.get(user=request.user)
    data = Vehicles.objects.filter(owner_name=u)
    return render(request,'vehicle_view_ow.html',{'data':data})

def update_vehicles(request,id):
    detail = Vehicles.objects.get(id=id)
    form = VehicleForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        messages.info(request, 'Vehicle Details Updated Successfully')
        return redirect('vehicle_view_ow')
    return render(request,'update_vehicles.html',{'form':form})

def del_vehicle_ow(request,id):
    data = Vehicles.objects.get(id=id)
    data.delete()
    return redirect('vehicle_view_ow')

def booking_view(request):
    data = BookVehicle.objects.all()
    return render(request,'booking_view.html',{'data':data})

def Ad_payment(request):
    u=Owner.objects.get(user=request.user)
    data = Payments.objects.filter(owner_name=u)
    return render(request,'Ad_payment.html',{'data':data})
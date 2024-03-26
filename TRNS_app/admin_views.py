from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from TRNS_app.forms import VehicleForm, ChatFormCUS
from TRNS_app.models import Customer, Vehicles, BookVehicle, CHAT_CUS, Feedback, Owner


def view_customers(request):
    data = Customer.objects.all()
    return render(request,'view_customers.html',{'data':data})

def view_owners(request):
    data = Owner.objects.all()
    return render(request,'view_owners.html',{'data':data})

def approve_cus(request,id):
    cus = Customer.objects.get(user_id=id)
    cus.approval_status = True
    cus.save()
    messages.info(request, 'approved')
    return redirect('view_customers')

def del_cus(request,id):
    data = Customer.objects.get(user_id=id)
    data.delete()
    return redirect('view_customers')



def vehicle_view(request):
    data = Vehicles.objects.all()
    return render(request,'vehicle_view.html',{'data':data})

def update_vehicles(request,id):
    detail = Vehicles.objects.get(id=id)
    form = VehicleForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        messages.info(request, 'Vehicle Details Updated Successfully')
        return redirect('vehicle_view')
    return render(request,'update_vehicles.html',{'form':form})

def del_vehicle(request,id):
    data = Vehicles.objects.get(id=id)
    data.delete()
    return redirect('vehicle_view')


def bookings(request):
    book = BookVehicle.objects.all()
    for i in book:
        i.seen = True
        i.save()
    request.session['booking'] = 0
    return render(request, 'bookings.html', {'books': book})

@login_required(login_url='accounts:login_view')
def confirm_booking(request, id):
    details_qs = Vehicles.objects.all()
    if details_qs.exists():

        book = BookVehicle.objects.get(id=id)
        book.status = 1
        book.save()
        messages.info(request, 'Vehicle Booking Confirmed')
        return redirect('bookings')
    else:
        messages.info(request, 'Please Update Vehicle Details')
        return HttpResponseRedirect(reverse('bookings'))

@login_required(login_url='accounts:login_view')
def reject_booking(request, id):
    book = BookVehicle.objects.get(id=id)
    if request.method == 'POST':
        book.status = 2
        book.save()
        messages.info(request, 'Vehicle Booking rejected')
        return redirect('bookings')
    return render(request, 'reject_booking.html')



def chat_add_ad(request):
    form = ChatFormCUS()
    u = request.user
    if request.method == 'POST':
        form = ChatFormCUS(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('chat_view_admin')
    else:
        form = ChatFormCUS()
    return render(request,'chat_add_ad.html',{'form':form})

def chat_view_admin(request):
    chats = CHAT_CUS.objects.all()
    return render(request, 'chat_view_admin.html', {'chats': chats})

@login_required(login_url='login_view')
def Feedback_CUS(request):
    f = Feedback.objects.all()
    return render(request, 'Feedback_CUS.html', {'feedback': f})


@login_required(login_url='login_view')
def reply_Feedback(request, id):
    f = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        f.reply = r
        f.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('Feedback_CUS')
    return render(request, 'reply_Feedback.html', {'feedback': f})

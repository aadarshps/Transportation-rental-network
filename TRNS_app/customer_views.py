from django.contrib import messages
from django.shortcuts import render, redirect

from TRNS_app.forms import CustomerBookVehicleForm, ChatFormCUS, FeedbackForm, PaymentForm
from TRNS_app.models import Vehicles, Customer, BookVehicle, CHAT_CUS, Feedback, Rent


def view_vehi(request):
    data = Vehicles.objects.all()
    return render(request,'view_vehi.html',{'data':data})

def book_vehicle(request):
    form = CustomerBookVehicleForm()
    if request.method == 'POST':
        form = CustomerBookVehicleForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)

            book.customer = Customer.objects.get(user=request.user)
            book.To_which_date = form.cleaned_data.get('To_which_date')
            book.booking_date = form.cleaned_data.get('booking_date')
            book.booked_by = request.user
            customer_qs = BookVehicle.objects.filter(customer=Customer.objects.get(user=request.user))
            if customer_qs.exists():
                messages.info(request, 'You have Already Booked room  ')
            else:
                book.save()
                messages.info(request, 'Successfully Booked Room ')
                return redirect('booking_status')
    return render(request, 'book_vehicle.html', {'form': form})

def booking_status(request):
    customer = Customer.objects.get(user=request.user)
    status = BookVehicle.objects.filter(customer=customer)
    return render(request, 'booking_status.html', {'statuss': status})

def chat_add_cus(request):
    form = ChatFormCUS()
    u = request.user
    if request.method == 'POST':
        form = ChatFormCUS(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('chat_view_cus')
    else:
        form = ChatFormCUS()
    return render(request,'chat_add_cus.html',{'form':form})

def chat_view_cus(request):
    u= request.user
    print(u)
    chat = CHAT_CUS.objects.exclude(user=u)
    chat1=CHAT_CUS.objects.filter(user=u)
    print(chat1)
    return render(request,'chat_view_cus.html',{'chat':chat,'chat1':chat1})

def Feedback_add_user(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('Feedback_view_user')
    return render(request, 'Feedback_add_user.html', {'form': form})

def Feedback_view_user(request):
    f = Feedback.objects.filter(user=request.user)
    return render(request, 'Feedback_view_user.html', {'feedback': f})

def pay_rent_fee(request):
    u=request.user
    form=PaymentForm()
    if request.method=='POST':
        form=PaymentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user=u
            data.save()
            return redirect('payment_view')
    return render(request,'pay_rent_fee.html',{'form':form})

def payment_view(request):
    data=Rent.objects.all()
    return render(request,'payment_view.html',{'data':data})



def viewAds(request):
    data = Vehicles.objects.all()
    return render(request,'Ads.html',{'data':data})
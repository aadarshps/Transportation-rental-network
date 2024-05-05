import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm

from TRNS_app.models import User, Customer, Vehicles, BookVehicle, CHAT_CUS, CHAT_AD, Feedback, Owner, Rent, Payments


class DateInput(forms.DateInput):
    input_type = 'date'

class UserReg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password',widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ('username','password1','password2')

class Customer_reg(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('user','approval_status')

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude=('user','approval_status')

class VehicleForm(forms.ModelForm):
    Insurance_EndDate = forms.DateField(widget=DateInput)
    class Meta:
        model = Vehicles
        exclude = ('owner_name',)

class CustomerBookVehicleForm(forms.ModelForm):
    To_which_date = forms.DateField(widget=DateInput)

    class Meta:
        model = BookVehicle
        fields = ('To_which_date','Vehicle')

        def clean_date_joining(self):
            date = self.cleaned_data['To_which_date']

            if date < datetime.date.today():
                raise forms.ValidationError("Invalid Date")
            return date

class ChatFormCUS(forms.ModelForm):
    class Meta:
        model = CHAT_CUS
        fields = ('desc',)

class ChatFormAD(forms.ModelForm):
    class Meta:
        model = CHAT_AD
        fields = ('desc',)

class FeedbackForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Feedback
        fields = ('subject', 'Enquiry', 'date')

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Rent
        exclude=('user',)

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'
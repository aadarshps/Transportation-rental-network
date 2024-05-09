from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="customer")
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=10)
    Email_Id = models.EmailField()
    Driving_License = models.ImageField(upload_to='DL')
    Adhar = models.ImageField(upload_to='ADHAR')
    approval_status = models.BooleanField(default=0)

    def __str__(self):
        return self.Name

class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Owner')
    Name = models.CharField(max_length=100)
    Place = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=10)
    Id_Proof = models.ImageField(upload_to='id_proof')
    approval_status = models.BooleanField(default=0)

    def __str__(self):
        return self.Name


f_type = (
    ('Petrol','Petrol'),
    ('Diesel','Diesel'),
    ('CNG','CNG'),
    ('Electric','Electric')
)

v_type = (
    ('Two Wheeler','Two Wheeler'),
    ('Three Wheeler','Three Wheeler'),
    ('Four Wheeler','Four Wheeler'),
    ('Six Wheeler','Six Wheeler')
)

class Vehicles(models.Model):
    owner_name = models.ForeignKey(Owner,on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=100,choices=v_type)
    Brand = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    condition = models.CharField(max_length=100)
    Fuel_type = models.CharField(max_length=100,choices=f_type)
    Rent_Amount = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='v_image')
    RC_book = models.ImageField(upload_to='rc_book')
    Insurance_EndDate = models.DateField()

    def full_name(self):
        return f"{self.Brand}, {self.Name}"

    def __str__(self):
        return self.full_name()

class BookVehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Vehicle = models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    To_which_date = models.DateField()
    booking_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)

class CHAT_CUS(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cus_chat',null=True)
    desc = models.TextField()
    date = models.DateField(auto_now=True)

class CHAT_AD(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='admin_chat',null=True)
    desc = models.TextField()
    date = models.DateField(auto_now=True)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    Enquiry = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)

class Rent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Payment',null=True)
    Card_Number=models.CharField(max_length=100)
    MM_YY=models.CharField(max_length=50)
    CVV=models.CharField(max_length=50)
    Name_on_the_card=models.CharField(max_length=50)
    Amount=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)

class Payments(models.Model):
    owner_name = models.ForeignKey(Owner,on_delete=models.CASCADE)
    Amount = models.CharField(max_length=10,null=True,blank=True)
    card_number = models.CharField(max_length=16)
    expiry = models.CharField(max_length=10)
    cvv = models.CharField(max_length=3)
    date = models.DateField(auto_now=True)

months = [
    ('1 month','1 month'),
    ('2 month','2 month'),
    ('3 month','3 month'),
]
class Subscription(models.Model):
    vehicle = models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    Months = models.CharField(max_length=100,choices=months)
    amount = models.CharField(max_length=100)

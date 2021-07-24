from django.db import models
from shortuuidfield import ShortUUIDField
from cloudinary.models import CloudinaryField
Status = (
    ('pickup', 'PICKUP'),
    ('processing', 'PROCESSING'),
    ('delivered', 'DELIVERED'),
)

Gender = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),  
)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False)
    subject = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Pickup(models.Model):
    uuid = ShortUUIDField()
    sendername = models.CharField(max_length=200,null=False)
    recivername = models.CharField(max_length=200,null=False)
    senderemail = models.CharField(max_length=200,null=False)
    reciveremail = models.CharField(max_length=200,null=False)
    senderphone = models.CharField(max_length=200,null=False)
    reciverphone = models.CharField(max_length=200,null=False)
    senderaddress = models.CharField(max_length=200,null=False)
    reciveraddress = models.CharField(max_length=200,null=False)
    senderlocation = models.CharField(max_length=200,null=False)
    reciverlocation = models.CharField(max_length=200,null=False)
    parcel = models.CharField(max_length=200,null=False)
    message = models.TextField(blank=True)
    status=models.CharField(max_length=200,null=False,choices=Status)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uuid

class RiderRecord(models.Model):
    fullname=models.CharField(max_length=200,null=False)
    gender=models.CharField(max_length=200,null=False,choices=Gender)
    state_of_origin=models.CharField(max_length=100,null=False)
    lga_of_origin=models.CharField(max_length=100,null=False)
    residential_address=models.CharField(max_length=400,null=False)
    residential_lga=models.CharField(max_length=200,null=False)
    residential_state=models.CharField(max_length=200,null=False)
    phone_no=models.CharField(max_length=11,null=False)
    bank_name=models.CharField(max_length=200,null=False)
    bank_account_no=models.CharField(max_length=200,null=False)
    image_of_rider=CloudinaryField('image')
    qualification=models.CharField(max_length=200,null=False)
    date_of_appointment=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class RiderAssignment (models.Model):
    rider_name= models.ForeignKey(RiderRecord, on_delete=models.DO_NOTHING,null=False,default=0)
    public_tracking_id=models.CharField(max_length=22,null=False)
    date_and_time_of_assignment=models.DateTimeField(auto_now_add=True)
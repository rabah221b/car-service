
from django.db import models

# Create your models here.

class classofvechiles(models.Model):
    class_name = models.CharField(max_length=100)
    class_description = models.TextField()
    
    def __str__(self):
        return self.class_name

class vechiles(models.Model):
    vehicle_name = models.CharField(max_length=255)
    vehicle_cc = models.CharField(max_length=255)
    class_name = models.ForeignKey(classofvechiles, on_delete=models.CASCADE)
    vehicle_img = models.ImageField(upload_to='vechiles')
    vehicle_price = models.IntegerField(default=150)
    
    def __str__(self):
            return 'VECHILES--'   + self.vehicle_name + '(' + self.vehicle_cc +')'

class booking(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_phone_number = models.CharField(max_length=10)
    customer_email = models.EmailField()
    vehicle_type = models.ForeignKey(vechiles, on_delete= models.CASCADE) 
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)


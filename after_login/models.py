from django.db import models
from accounts.models import MyUser
from django.conf import settings
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserEdit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,unique=True)
    adress = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    model_pic = models.ImageField(default='empty_profile.png',null=True, blank=True)
    phone_number = PhoneNumberField()

class Transactions(models.Model):
    CHOICES = [
        ('Purchased','Buy'),
        ('Sale','Sell'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    type = models.CharField(max_length=12, choices=CHOICES)
    quantity = models.PositiveIntegerField()
    invested = models.FloatField()
    actual_invested = models.FloatField()
    company = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    profit = models.FloatField()

class companies(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    company_simbol = models.CharField(max_length=10)
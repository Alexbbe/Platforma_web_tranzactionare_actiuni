from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from datetime import datetime

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self,email,username,birth_date,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")
        if not birth_date:
            raise ValueError("User must have birth date")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            birth_date=birth_date
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,birth_date,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            birth_date = birth_date
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email                   = models.EmailField(verbose_name="email",max_length=100,unique=True)
    username                = models.CharField(max_length=60,unique=True)
    data_joined             = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    birth_date              = models.DateField(verbose_name="birth date")
    first_name              = models.CharField(max_length=100)
    last_name               = models.CharField(max_length=100)
    money                   = models.FloatField(default=1000000)
    company_list               = models.JSONField(default={'AAPL':'Apple Inc','TSLA':'Tesla Inc','PFE':'Pfizer Inc'})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','birth_date']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True






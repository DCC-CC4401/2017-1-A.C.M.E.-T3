from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    cost = models.IntegerField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    stock = models.IntegerField()
    category = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos', blank=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class VendedorFijoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    init_time = models.TimeField()
    end_time = models.TimeField()
    likes = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(upload_to='photos', blank=True)
    cash = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    student = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class VendedorAmbProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='photos', blank=True)
    likes = models.PositiveIntegerField(default=0)
    cash = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    student = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='photos', blank=True)
    favVendFijo = models.ManyToManyField(VendedorFijoProfile, blank=True)
    favVendAmb = models.ManyToManyField(VendedorAmbProfile, blank=True)

    def __str__(self):
        return self.user.username

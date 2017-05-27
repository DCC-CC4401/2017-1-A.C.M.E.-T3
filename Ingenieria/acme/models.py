from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    cost = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    stock = models.PositiveIntegerField()
    avatar = models.ImageField(default="acme/img/pollo1.png")
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="acme/img/AvatarEstudiante.png")

    def __str__(self):
        return self.user.username

class VendedorFijoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    init_time = models.TimeField()
    end_time = models.TimeField()
    likes = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(default="acme/img/AvatarVendedor1.png")
    #dishes = models.ManyToManyField(Product, blank=True)
    favorites = models.ManyToManyField(ClientProfile, blank=True)
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    student = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class VendedorAmbProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check = models.BooleanField(default=False)
    avatar = models.ImageField(default="acme/img/AvatarVendedor4.png")
    #dishes = models.ManyToManyField(Product, blank=True)
    likes = models.PositiveIntegerField(default=0)
    favorites = models.ManyToManyField(ClientProfile, blank=True)
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    student = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

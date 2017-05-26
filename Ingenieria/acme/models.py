from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    return "%s/%s" % (new_id, filename)

class Product(models.Model):
    cost = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    stock = models.PositiveIntegerField()
    #avatar = models.ImageField(upload_to=upload_location)


class Payment(models.Model):
    name = models.CharField(max_length=30)


class VendedorFijoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    init_time = models.TimeField()
    end_time = models.TimeField()
    likes = models.PositiveIntegerField(default=0)
    #avatar = models.ImageField(upload_to=upload_location)
    dishes = models.ManyToManyField(Product)
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    student = models.BooleanField(default=False)

    def set_avatar(self):
        _avatar = self.avatar
        if not _avatar:
            self.avatar = "acme/img/AvatarEstudiante.png"


class VendedorAmbProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check = models.BooleanField(default=False)
    #avatar = models.ImageField(upload_to=upload_location)
    dishes = models.ManyToManyField(Product)
    likes = models.PositiveIntegerField(default=0)
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    student = models.BooleanField(default=False)

    def set_avatar(self):
        _avatar = self.avatar
        if not _avatar:
            self.avatar = "acme/img/AvatarEstudiante.png"


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=upload_location)

    def set_avatar(self):
        _avatar = self.avatar
        if not _avatar:
            self.avatar = "acme/img/AvatarEstudiante.png"


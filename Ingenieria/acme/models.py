from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    cost = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    stock = models.PositiveIntegerField()
    # avatar = models.ImageField()


class Payment(models.Model):
    name = models.CharField(max_length=30)


class VendedorFijoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    init_time = models.TimeField()
    end_time = models.TimeField()
    likes = models.PositiveIntegerField()
    # avatar = models.ImageField()
    #  dishes = models.ForeignKey(Product)
    # payment = models.ForeignKey(Payment)

# class VendedorAmbProfile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#  check = models.BooleanField()
# avatar = models.ImageField()

#    @receiver(post_save, sender=User)
#   def create_user_profile(sender, instance, created, **kwargs):
#      if created:
#         UserProfile.objects.create(user=instance)

#    @receiver(post_save, sender=User)
#   def save_user_profile(sender, instance, **kwargs):
#      instance.profile.save()


def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    return "%s/%s" % (new_id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=upload_location)

    def set_avatar(self):
        _avatar = self.avatar
        if not _avatar:
            self.avatar = "acme/img/AvatarEstudiante.png"

# @receiver(post_save, sender=User)
#    def create_user_profile(sender, instance, created, **kwargs):
#        if created:
#            Profile.objects.create(user=instance)

#    @receiver(post_save, sender=User)
#    def save_user_profile(sender, instance, **kwargs):
#        instance.profile.save()

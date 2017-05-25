from __future__ import  unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


#class UserProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    avatar = models.ImageField()

#    @receiver(post_save, sender=User)
 #   def create_user_profile(sender, instance, created, **kwargs):
  #      if created:
   #         UserProfile.objects.create(user=instance)

    #@receiver(post_save, sender=User)
#    def save_user_profile(sender, instance, **kwargs):
 #       instance.profile.save()

#class VendedorFijoProfile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  init_time = models.DateTimeField()
   # end_time = models.DateTimeField()
    #avatar = models.ImageField()
  #  platos = models.ForeignKey

#    @receiver(post_save, sender=User)
 #   def create_user_profile(sender, instance, created, **kwargs):
  #      if created:
   #         UserProfile.objects.create(user=instance)

    #@receiver(post_save, sender=User)
 #   def save_user_profile(sender, instance, **kwargs):
  #      instance.profile.save()

   # def update_profile(request, user_id):
    #    user = User.objects.get(pk=user_id)
     #   user.save()

#class VendedorAmbProfile(models.Model):
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
    return "%s/%s" %(new_id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=upload_location)

    def set_avatar(self):
        _avatar = self.avatar
        if not _avatar:
            self.avatar = "acme/img/AvatarEstudiante.png"

#    @receiver(post_save, sender=User)
#    def create_user_profile(sender, instance, created, **kwargs):
#        if created:
#            Profile.objects.create(user=instance)

#    @receiver(post_save, sender=User)
#    def save_user_profile(sender, instance, **kwargs):
#        instance.profile.save()


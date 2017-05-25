# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from acme.models import VendedorFijoProfile, UserProfile

admin.site.register(VendedorFijoProfile)
admin.site.register(UserProfile)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from acme.models import VendedorFijoProfile, ClientProfile, VendedorAmbProfile, Product

admin.site.register(VendedorFijoProfile)
admin.site.register(ClientProfile)
admin.site.register(VendedorAmbProfile)
admin.site.register(Product)

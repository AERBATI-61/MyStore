from django.contrib import admin
from .models import *

admin.site.register(Seller)
admin.site.register(City)
admin.site.register(Payment)
admin.site.register(Invoice)
admin.site.register(Tax)
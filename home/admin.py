from django.contrib import admin
from home.models import *
# Register your models here.


class DronzaHome(admin.ModelAdmin):
    pass

admin.site.register(hello, DronzaHome)
admin.site.register(contact_us, DronzaHome)
admin.site.register(productReview, DronzaHome)
admin.site.register(Place_Order, DronzaHome)
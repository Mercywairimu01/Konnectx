from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Distributor)
admin.site.register(Profile)
admin.site.register(DProfile)



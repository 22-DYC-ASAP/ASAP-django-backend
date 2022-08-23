from django.contrib import admin
from .models import BurnDegree, Result, AddressInfo, BurnInfo, BurnPic

# Register your models here.

admin.site.register(BurnDegree)
admin.site.register(Result)
admin.site.register(AddressInfo)
#admin.site.register(PickType)
admin.site.register(BurnInfo)
admin.site.register(BurnPic)
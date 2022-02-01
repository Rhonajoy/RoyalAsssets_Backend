from django.contrib import admin
from .models import Profile, RequestAsset,Asset,Role,Add_staff
from .models import User

# Register your models here.
admin.site.register(RequestAsset)
admin.site.register(Asset)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Add_staff)


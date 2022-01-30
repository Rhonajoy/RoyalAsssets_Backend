from django.contrib import admin
from .models import RequestAsset,Asset
from .models import User

# Register your models here.
admin.site.register(RequestAsset)
admin.site.register(Asset)
admin.site.register(User)


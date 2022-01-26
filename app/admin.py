from urllib.request import Request
from django.contrib import admin

from .models import Asset, Characteristics, User, Request


admin.site.register(User)
admin.site.register(Characteristics)
admin.site.register(Asset)
admin.site.register(Request)


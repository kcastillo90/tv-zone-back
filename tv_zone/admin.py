from django.contrib import admin

# Register your models here.
from .models import Shows
admin.site.register(Shows)

from .models import Users
admin.site.register(Users)

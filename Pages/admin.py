from django.contrib import admin
from .models import Account, Tutorial , Models
# Register your models here.
admin.site.register(Tutorial)
admin.site.register(Account)
admin.site.register(Models)
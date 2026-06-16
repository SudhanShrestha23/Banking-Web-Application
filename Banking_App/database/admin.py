from django.contrib import admin
from .models import UserProfile, BankAccount, Transaction
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BankAccount)
admin.site.register(Transaction)
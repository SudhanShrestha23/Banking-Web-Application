from django.contrib import admin
from .models import UserProfile, BankAccount, Transactions
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BankAccount)
admin.site.register(Transactions)
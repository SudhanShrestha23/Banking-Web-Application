from django.db import models

# Create your models here.

# Users are either a customer or an admin
class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.IntegerField(default=0, primary_key=True)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField()

    def __str__(self):
        return str(self.user_id)

# Belongs to users
class BankAccount(models.Model):
    account_id = models.IntegerField(default=0, primary_key=True)
    balance = models.FloatField(default=0)
    account_type = models.CharField(max_length=200)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(self.account_id)

# Has two account IDs. One for sender and reciever
class Transaction(models.Model):
    transaction_id = models.IntegerField(default=0, primary_key=True)
    sender_account_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE, default=0)
    amount = models.FloatField(default=0)
    transation_date = models.FloatField(default=0)
    transaction_type = models.CharField(max_length=200, default='')
    receiver_account_id = models.CharField(max_length=10, default='')

    def __str__(self):
        return str(self.transaction_id)

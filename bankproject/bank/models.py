from django.db import models

class Application(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    ACCOUNT_TYPE_CHOICES = [
        ('SA', 'Savings Account'),
        ('CA', 'Current Account'),
    ]
    BRANCH_TYPE_CHOICES = [
        ('B1','Branch 1'),
        ('B2','Branch 2')
    ]
    DISTRICT_TYPE_CHOICES = [
        ('D1','TRIVANDRUM'),
        ('D2','KOLLAM'),
        ('D3','ALAPPUZHA'),
        ('D4','ERNAKULAM'),
        ('D5', 'KOZHIKODE'),
    ]

    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100,choices=DISTRICT_TYPE_CHOICES)
    branch = models.CharField(max_length=100, choices=BRANCH_TYPE_CHOICES)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE_CHOICES)
    debit_card = models.BooleanField(default=False)
    credit_card = models.BooleanField(default=False)
    cheque_book = models.BooleanField(default=False)

    def __str__(self):
        return self.name

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
Users = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=50)
    mentor = models.CharField(max_length=100)
    assistant = models.CharField(max_length=100)
    classroom = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.FloatField(verbose_name='Price')
    time = models.FloatField(verbose_name='Time')


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    pin = models.IntegerField(validators=[
            MaxValueValidator(9999),
            MinValueValidator(1000)
        ]
     )
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)


class User(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    pin = models.IntegerField(validators=[
            MaxValueValidator(999999),
            MinValueValidator(100000)
        ]
     )
    active = models.BooleanField(default=True)


class Buffet(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='img/buffet/pic', blank=True, null=True)
    price = models.FloatField()
    active = models.BooleanField(default=True)


class OperationDetail(models.Model):
    buffet = models.ForeignKey(Buffet, on_delete=models.DO_NOTHING)
    operation = models.ForeignKey('Operation', on_delete=models.DO_NOTHING)
    amount = models.IntegerField()


class Operation(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    sum = models.FloatField()
    debt_sum = models.FloatField()
    STATUS_CHOICES = [(0, 'Оплачен'),
                      (1, 'Не оплачен'),
                      (2, 'Списанный')]

    status = models.IntegerField(choices=STATUS_CHOICES)
    pin = models.ForeignKey('Pin', on_delete=models.DO_NOTHING, related_name='Pin')


class Pin(models.Model):
    pin = models.IntegerField()
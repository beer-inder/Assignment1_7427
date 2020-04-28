from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class extendeduser(models.Model):
    phone_num = models.CharField(max_length=15)
    location = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ExtendedUser"

    def __str__(self):
        return f'{self.user.username}'

    @property
    def username(self):
        return self.user.username


class child(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    child_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    child_age = models.IntegerField()
    sex = {
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    }
    gender = models.CharField(max_length=20, choices=sex, default='male')
    date_of_birth = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    guardian = models.CharField(max_length=50)
    relation_guardian = models.CharField(max_length=20)
    enrolment_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Child"

    def __str__(self):
        return self.child_name

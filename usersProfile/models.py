from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class extendeduser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_num = models.CharField(max_length=15)
    image = models.ImageField(upload_to='photos/', blank=True)
    location = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "ExtendedUser"

    def __str__(self):
        return f'{self.user.username}'

    @property
    def username(self):
        return self.user.username


class guardian(models.Model):
    guardian_name = models.CharField(max_length=50)
    relation_guardian = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=15)

    def __str__(self):
        return self.guardian_name


class child(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    child_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    child_age = models.IntegerField(null=True, blank=True)
    sex = {
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    }
    gender = models.CharField(max_length=20, choices=sex, default='male')
    date_of_birth = models.DateField(max_length=20)
    nationality = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    guardian_name = models.ForeignKey(
        guardian, on_delete=models.SET_NULL, null=True)
    photo_main = models.ImageField(upload_to='photos/')
    photo_1 = models.ImageField(upload_to='photos/', blank=True)
    enrolment_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Child"

    def __str__(self):
        return self.child_name


class activity(models.Model):
    #    teacher_name = models.ForeignKey(
    #        User, related_name='teacher_name', on_delete=models.SET_NULL, null=True)
    teacher_name = models.CharField(max_length=100)
    children_list = models.ManyToManyField(child)
    activity_name = models.CharField(max_length=500)
    activity_description = models.CharField(max_length=1000)
    activity_Date = models.DateField()
    activity_duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "Activity"

    def __str__(self):
        return self.activity_name


# Command to get list of children enrolled in an activity
        # ch=activity.objects.filter(children_list__child_name="child2beer")


class teacher(models.Model):
    pass


class newsletter(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class notification(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

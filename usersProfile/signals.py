from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import extendeduser, child, activity, notification
from django.core.mail import send_mail
from .views import send_signup_mail


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        extendeduser.objects.create(user=instance)
        email = 'beerinder.mca@gmail.com'
        subject = "Thank You for Joining Kindergarten"
        from_email = settings.EMAIL_HOST_USER
        r_email = email
        signup_message = """Welcome to KinderGarten !!!!!!"""


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.extendeduser.save()
    email = instance.email
    eamil_instance = notification.objects.create(email=email)
    eamil_instance.save()
    signup_message = """Welcome to KinderGarten !!!!!!"""
#    send_signup_mail(email, signup_message)


@receiver(post_save, sender=activity)
def update_child_model(sender, instance, **kwargs):
    print("****************** Do Something ***************")

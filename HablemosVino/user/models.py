from django.db import models
from django.contrib.auth.models import AbstractUser
#Importaciones para mandar mails
from django.db.models.signals import post_save
from django.dispatch import receiver
from decouple import config
from django.core.mail import send_mail

# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=256)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='Profiles', blank=True, null=True,)
    profession = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    birthday = models.DateField(null=True)
    twitter = models.URLField(max_length=50, null=True, blank=True)
    linkedin = models.URLField(max_length=50, null=True, blank=True)
    facebook = models.URLField(max_length=50, null=True, blank= True)

    def __str__(self):
        return self.user.username
#Crear una señal de que un usauario se registro
@receiver(post_save, sender=User)
def email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Bienvenido a Abc Blog',
            str('Hola' + instance.full_name + ', usted se ha registrado satisfacoriamente en el blog.'
                                                'Es un placer que seas parte de nuestra familia'),
            config('EMAIL_HOST_USER'),
            [instance.email]
        )
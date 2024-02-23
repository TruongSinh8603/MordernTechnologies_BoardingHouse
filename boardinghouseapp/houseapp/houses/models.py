from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

class User(AbstractUser):
    RENTER = 1
    LANDLORD = 2
    ADMIN = 3

    ROLE_CHOICES = [
        (RENTER, "Renter"),
        (LANDLORD, "Landlord"),
        (ADMIN, "Admin"),
    ]

    phonenumber = models.CharField(max_length=20, null=False)
    email = models.EmailField("email_address", null=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=RENTER)
    avatar = CloudinaryField('avatar', null=False)
    groups = models.ManyToManyField(Group, related_name='auth_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='auth_user_set')

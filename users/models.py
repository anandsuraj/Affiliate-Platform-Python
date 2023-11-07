from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    # Add any additional fields you need for your user model
    # For example:
    # full_name = models.CharField(max_length=255)
    # date_of_birth = models.DateField(null=True, blank=True)

    # Specify the user's unique identifier field
    USERNAME_FIELD = 'email'
    # Add any other fields required for authentication, such as 'password' or 'username'

    # Define the required fields for creating a user
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
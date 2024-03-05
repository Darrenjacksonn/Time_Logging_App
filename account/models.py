from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def user_creation(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not password:
            raise ValueError(_('The Password field must be set'))
                             
        email = self.normalize_email(email) # convert email to lowercase
        user = self.model(email=email, **extra_fields) # extra fields include any other fields that are passed in the CustomUser model (eg. first_name)
        user.set_password(password) # sets the password, django handles password hashing
        return user

    def create_user(self, email, password, **extra_fields):
        user = self.user_creation(email, password, **extra_fields)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db) # saves the user to the database
        return user # returns the user in case you want to do something with it immediately after creating it

    def create_staff_user(self, email, password, **extra_fields):
        """Create and return a superuser with an email and password."""
        user = self.user_creation(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = False

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and return a superuser with an email and password."""
        user = self.user_creation(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db) 
        return user






class CustomUser(AbstractBaseUser, PermissionsMixin):
    """User model that extends AbstractBaseUser and replaces username with email."""
    email = models.EmailField(_('email address'), unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    name = models.CharField(max_length=30, blank=True)
    

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin,
)
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator


# User manager class
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, full_name, password, phone, user_status, **extra_fields):
        # Checking email
        if not email:
            raise ValueError("You have not entered an email!")
        # Checking full name
        if not full_name:
            raise ValueError("You have not entered a full name!")
        # Checking phone
        if not phone:
            raise ValueError("You have not entered a phone number!")
        if not user_status:
            raise ValueError("You have not entered a user status: Admin, CEO, CTO, Designer,\
              Product Owner, Programmer, Project Manager, QA!")
        # Create a user
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            full_name=full_name,
            user_status=user_status,
            **extra_fields,
        )
        # Save the password
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Creating a regular user
    def create_user(self, email, full_name, phone, user_status, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False),
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(email, full_name, phone, user_status, password, **extra_fields)

    # Creating a site administrator
    def create_superuser(self, email, full_name, password, phone, user_status, **extra_fields):
        extra_fields.setdefault('is_staff', True),
        extra_fields.setdefault('is_superuser', True),
        extra_fields.setdefault('is_active', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, full_name, password, phone, user_status, **extra_fields)


# Creating the User class
class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=160)  # Name and Surname
    email = models.EmailField(max_length=150, unique=True)  # Email
    is_active = models.BooleanField(default=False)  # Activation status
    user_status = models.CharField(
        max_length=15, choices=(
            ('Admin', 'Admin'), ('CEO', 'CEO'), ('CTO', 'CTO'),
            ('Designer', 'Designer'), ('Product Owner', 'Product Owner'),
            ('Programmer', 'Programmer'), ('Project Manager', 'Project Manager'),
            ('QA', 'QA'),
        ),
        validators=[MinLengthValidator(2)]
    )  # User status
    is_staff = models.BooleanField(default=False)  # Administrator status
    date_joined = models.DateTimeField(name='registered', auto_now_add=True, editable=True)  # Date registration
    phone = PhoneNumberField(unique=True, max_length=16)  # Phone number

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone', 'is_active', 'user_status']  # List of field names for Superuser

    objects = CustomUserManager()

    def __repr__(self):
        return User.__name__

    class Meta:
        ordering = ['email']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

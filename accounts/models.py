from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, staff_category='manager', **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, staff_category=staff_category, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        # For a superuser, we set the staff_category to 'supperadmin' (or whatever name you prefer)
        extra_fields.setdefault('staff_category', 'supperadmin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('staff_category') != 'supperadmin':
            raise ValueError("Superusers must have staff_category of 'supperadmin'")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    STAFF_CATEGORY_CHOICES = (
        ('supperadmin', 'Super Admin'),
        ('ceo', 'CEO'),
        ('accountant', 'Accountant'),
        ('manager', 'Manager'),
    )
    
    email = models.EmailField(unique=True)
    staff_category = models.CharField(max_length=50, choices=STAFF_CATEGORY_CHOICES, default='manager')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # You can add additional fields here if needed

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & password are required by default.

    def __str__(self):
        return self.email

    def can_reset_password(self):
        """
        Returns True if the user is allowed to reset other users' passwords.
        In this case, only a 'supperadmin' is permitted.
        """
        return self.staff_category == 'supperadmin'

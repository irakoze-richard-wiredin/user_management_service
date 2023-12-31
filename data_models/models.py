from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, email=None, **extra_fields):
        if not username:
            raise ValueError("You have not provided a valid e-mail address")
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        UserProfile.objects.create(user=user)
        AccountVerification.objects.create(user=user)

        return user
    
    def create_user(self, username=None, password=None, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('first_login', True)
        return self._create_user(username, password, email, **extra_fields)
    
    def create_superuser(self, username=None, password=None, email=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('first_login', False)
        extra_fields.setdefault('first_name', 'Super')
        extra_fields.setdefault('last_name', 'Admin')
        return self._create_user(username, password, email, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(blank=True, default='', unique=True)  
    first_name = models.CharField(max_length = 250, null=False, blank=True)
    last_name = models.CharField(max_length = 250, null=False, blank=True)
    
    email = models.CharField(max_length = 250, null=False, blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    first_login = models.BooleanField(default=True, null=True, blank=True) 
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='user_permissions'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return str(self.last_name) + ' ' + str(self.first_name)
    
    def get_short_name(self):
        return str(self.last_name)
    
    def get_permission(self):
        if(self.is_superuser):
            permissions = list(Permission.objects.all().values_list('codename', flat=True))
        else:
            permissions = list({codename for group in self.groups.all() for codename in group.permissions.values_list('codename', flat=True)})
        
        return permissions

   
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    marital_status = models.CharField(max_length=20, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"


class AccountVerification(models.Model):
    VERIFICATION_CHOICES = [
        ('unverified', 'Unverified'),
        ('pending', 'Pending Verification'),
        ('verified', 'Verified'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_CHOICES, default='unverified')
    nid_passport_number = models.CharField(max_length=50, blank=True, null=True)
    document_image = models.ImageField(upload_to='verification_documents/', blank=True, null=True)
    verification_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Verification"


class Notifications(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]

    recipient = models.CharField(max_length=250, null=False)
    subject = models.CharField(max_length=5000, null=True, blank=True)
    body = models.CharField(max_length=5000, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.recipient}'s notification"


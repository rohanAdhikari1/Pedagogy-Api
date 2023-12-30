from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import  PermissionsMixin,AbstractBaseUser
from .manager import UserManager
from django.utils.html import format_html





##########################################################
        





##########################################################
        

###Model for all User

class BaseUser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    username = None
    email = None
    USER_ROLES = (
        ('student', 'Student'),
        ('tutor', 'Tutor'),
        ('admin', 'Admin'),
        ('superadmin', 'SuperAdmin'),
    )
    id = models.AutoField(primary_key=True)
    phone = models.IntegerField(_("Phone"),validators=[MaxValueValidator(9999999999)],unique=True)
    name = models.CharField(_("name"),max_length=50,default="")
    email = models.EmailField(_("Email"),blank=True)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile = models.ImageField(upload_to="profile/",default="profile/default.jpg",null=True,blank=True)

    USERNAME_FIELD ='phone'
    REQUIRED_FIELDS =[]
    def has_module_perms(self, app_label):
       return self.is_superadmin
    def has_perm(self, perm, obj=None):
       return self.is_superadmin
    def __str__(self):
        return str(self.id)
    def profile_image(self):
            return format_html('<img src="{}" width="50" height="50" />', self.profile)
    profile_image.allow_tags = True






##########################################################
        





##########################################################
        

###Base Model for all Model
class BaseModel(models.Model):
    uid = models.UUIDField(editable=False, default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True






##########################################################
        





##########################################################
        


#Student or parent Model
class Student(BaseModel,BaseUser):
    parent_name = models.CharField(_("Parent Name"),max_length=50)
    school = models.CharField(_("School"),max_length=150)
    class_name = models.CharField(_("Class Name"),max_length=50)
    address = models.CharField(_("Address"),max_length=150)
    landmark = models.CharField(_("Landmark"),max_length=240)
    board = models.CharField(_("Board"),max_length=50)
    def profile_image(self):
            return format_html('<img src="{}" width="50" height="50" />', self.profile.url)
    profile_image.allow_tags = True





##########################################################
        





##########################################################
        


#Tutor Model
class Tutor(BaseModel,BaseUser):
    YEAR_EXP = (
        ('below 1 year', 'Below 1 Year'),
        ('1 year', '1 Year'),
        ('2 Year', '2 Year'),
        ('3 Year', '3 Year'),
        ('4 Year', '4 Year'),
        ('5 Year', '5 Year'),
        ('Above 5 Year', 'Above 5 Year'),
    )
    HIGH_QUAL = (
        ('+2', '+2'),
        ('bachlor', 'Bachlor'),
        ('master', 'Master'),
        ('phd', 'Phd'),
    )
    AVAILABILITY_CHOICES = [
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        ('both', 'Both'),
        ('reserved', 'Reserved'),
    ]
    class_range = models.CharField(_("Class Range"),max_length=20)
    address = models.CharField(_("Address"),max_length=150)
    landmark = models.CharField(_("Landmark"),max_length=240)
    cgpa_see = models.FloatField(_("SEE CGPA"))
    cgpa_plus2 = models.FloatField(_("+2 CGPA"))
    cgpa_bachlor = models.FloatField(_("Bachlor CGPA"),blank=True)
    cgpa_master = models.FloatField(_("Master CGPA"),blank=True)
    citizenship_front = models.ImageField(upload_to="documents/",null=True,blank=True)
    citizenship_back = models.ImageField(upload_to="documents/",null=True,blank=True)
    high_degree = models.ImageField(upload_to="documents/",null=True,blank=True)
    high_degree_qual = models.CharField(max_length=40,choices=HIGH_QUAL)
    avaiable_time = models.CharField(max_length=10, choices=AVAILABILITY_CHOICES)
    is_professional = models.BooleanField(default=False)
    year_exp = models.CharField(choices=YEAR_EXP,max_length=20)
    def profile_image(self):
            return format_html('<img src="{}" width="50" height="50" />', self.profile.url)
    def citizenship_front_image(self):
            return format_html('<img src="{}" width="50" height="50" />', self.citizenship_front.url)
    citizenship_front.allow_tags = True
    def citizenship_back_image(self):
            return format_html('<img src="{}" width="50" height="50" />', self.citizenship_back.url)
    citizenship_back.allow_tags = True
    def high_degree_image(self):
            return format_html('<img src="{}" width="50" height="50" />', self.high_degree.url)
    high_degree.allow_tags = True







##########################################################
        





##########################################################
        

###Model for Notification
    
class Notifications(BaseModel):
    GROUP = (
        ('student', 'Student'),
        ('tutor', 'Tutor'),
        ('admin', 'Admin'),
        ('all', 'All'),
    )
    id = models.AutoField(primary_key=True)
    group = models.CharField(max_length=10, choices=GROUP)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'



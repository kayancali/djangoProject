from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(blank=True, max_length=30)
    description = models.CharField(blank=True, max_length=255)
    keywords = models.CharField(blank=True, max_length=255)
    company = models.CharField(blank=True, max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    instagaram = models.CharField(blank=True, max_length=30)
    twitter = models.CharField(blank=True, max_length=30)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    referances = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.title



class UserProfile(models.Model):


    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/users/')
    name = models.CharField(blank=True, max_length=20)
    def __str__(self):
        return self.user.username













from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    STATUS= (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()

    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


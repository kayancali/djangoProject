# Generated by Django 4.1.4 on 2022-12-25 18:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_images_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="detail",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Setting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("update_at", models.DateTimeField(auto_created=True)),
                ("create_at", models.DateTimeField(auto_created=True)),
                ("title", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=255)),
                ("keywords", models.CharField(max_length=255)),
                ("company", models.CharField(blank=True, max_length=50)),
                ("address", models.CharField(blank=True, max_length=150)),
                ("phone", models.CharField(blank=True, max_length=15)),
                ("fax", models.CharField(blank=True, max_length=15)),
                ("email", models.CharField(blank=True, max_length=50)),
                ("smtpserver", models.CharField(max_length=20)),
                ("smtpemail", models.CharField(max_length=20)),
                ("smtppassword", models.CharField(max_length=10)),
                ("smtpport", models.CharField(blank=True, max_length=5)),
                ("icon", models.ImageField(blank=True, upload_to="images/")),
                ("instagaram", models.CharField(max_length=30)),
                ("twitter", models.CharField(max_length=30)),
                ("aboutus", models.TextField()),
                ("referances", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[("True", "Evet"), ("False", "Hayır")], max_length=10
                    ),
                ),
            ],
        ),
    ]

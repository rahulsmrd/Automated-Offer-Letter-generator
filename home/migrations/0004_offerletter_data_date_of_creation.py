# Generated by Django 4.2.6 on 2023-11-18 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerletter_data',
            name='date_of_creation',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]

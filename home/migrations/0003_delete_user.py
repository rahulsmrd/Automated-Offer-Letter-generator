# Generated by Django 4.2.6 on 2023-10-30 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_name_offerletter_data_full_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

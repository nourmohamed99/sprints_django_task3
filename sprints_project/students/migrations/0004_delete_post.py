# Generated by Django 4.2.1 on 2023-05-16 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
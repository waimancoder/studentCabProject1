# Generated by Django 4.1.6 on 2023-02-05 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_newuser_dummy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='dummy',
        ),
    ]
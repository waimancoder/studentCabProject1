# Generated by Django 4.1.6 on 2023-02-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='dummy',
            field=models.BooleanField(default=False),
        ),
    ]
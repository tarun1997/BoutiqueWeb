# Generated by Django 2.0.6 on 2018-06-29 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_profile_email_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-24 09:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfil',
            new_name='UserProfile',
        ),
    ]

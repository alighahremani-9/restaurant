# Generated by Django 4.2.6 on 2023-10-25 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='username',
            new_name='user',
        ),
    ]

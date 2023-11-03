# Generated by Django 4.2.6 on 2023-10-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='message',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='phone',
        ),
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]

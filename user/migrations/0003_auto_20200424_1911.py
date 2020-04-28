# Generated by Django 3.0.3 on 2020-04-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_is_buyer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_buyer',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(default='Buyer', max_length=100),
            preserve_default=False,
        ),
    ]

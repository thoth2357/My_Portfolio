# Generated by Django 3.2.5 on 2022-01-25 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20220125_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='Social_media_info',
        ),
        migrations.AddField(
            model_name='social_media_info',
            name='user_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.user_info', verbose_name='user info'),
        ),
    ]

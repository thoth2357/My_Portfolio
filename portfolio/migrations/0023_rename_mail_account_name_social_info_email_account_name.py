# Generated by Django 3.2.5 on 2022-01-25 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_social_info_portfolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social_info',
            old_name='Mail_account_name',
            new_name='EMail_account_name',
        ),
    ]

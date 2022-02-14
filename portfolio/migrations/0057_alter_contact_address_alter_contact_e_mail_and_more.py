# Generated by Django 4.0.1 on 2022-02-14 19:58

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0056_portfolioexhibit_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Address',
            field=models.TextField(help_text='Contact Address', verbose_name='Address of Contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='E_mail',
            field=models.EmailField(max_length=254, verbose_name='Contact E-Mail'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number to display on home page', max_length=128, region=None, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Website',
            field=models.URLField(help_text='Website Link', verbose_name='Website Link'),
        ),
    ]

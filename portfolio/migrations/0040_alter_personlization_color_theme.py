# Generated by Django 3.2.5 on 2022-01-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0039_alter_personlization_color_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personlization',
            name='Color_theme',
            field=models.CharField(choices=[('yellow', 'yellow'), ('RED', 'RED'), ('BLUE', 'BLUE'), ('ORANGE', 'ORANGE')], default='Choose color theme', help_text='Choose the portfolio color scheme', max_length=50, verbose_name='Color Theme for Portfolio Colors'),
        ),
    ]

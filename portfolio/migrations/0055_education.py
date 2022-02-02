# Generated by Django 4.0.1 on 2022-02-02 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0054_remove_experience_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year_of_graduation', models.DateField(verbose_name='Year of graduation')),
                ('Degree_awarded', models.CharField(max_length=50, verbose_name='Degree Awarded')),
                ('Description', models.TextField(verbose_name='Description of degree awarded')),
                ('Experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.experience', verbose_name='User Experience')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
    ]

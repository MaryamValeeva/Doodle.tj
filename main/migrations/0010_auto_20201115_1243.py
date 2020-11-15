# Generated by Django 3.1.2 on 2020-11-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_development'),
    ]

    operations = [
        migrations.AddField(
            model_name='development',
            name='svg',
            field=models.CharField(default=0, max_length=5000, verbose_name='Svg'),
        ),
        migrations.AlterField(
            model_name='development',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='development',
            name='text',
            field=models.CharField(max_length=200, verbose_name='text'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201110_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_words', models.CharField(max_length=150, verbose_name='main_words')),
                ('sub_words', models.CharField(max_length=150, verbose_name='sub_words')),
            ],
        ),
        migrations.AlterField(
            model_name='technologies',
            name='svg',
            field=models.CharField(max_length=105000, verbose_name='Svg'),
        ),
    ]

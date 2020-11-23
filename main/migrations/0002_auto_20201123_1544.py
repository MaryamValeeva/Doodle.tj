# Generated by Django 3.1.2 on 2020-11-23 10:44

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.CharField(max_length=500, verbose_name='About us')),
                ('history', models.CharField(max_length=1000, verbose_name='History')),
                ('znachenie_nazvaniya', models.CharField(max_length=500, verbose_name='Znachenie_nazvaniya')),
                ('princips_of_work', models.CharField(max_length=500, verbose_name='Princips_of_work')),
            ],
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('text', models.CharField(max_length=200, verbose_name='text')),
                ('svg', models.CharField(default=0, max_length=5000, verbose_name='Svg')),
                ('position', models.IntegerField(default=0, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='FrameworkCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('text', models.CharField(max_length=1000, verbose_name='Text')),
                ('position', models.IntegerField(default=0, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_words', models.CharField(max_length=150, verbose_name='main_words')),
                ('sub_words', models.CharField(max_length=150, verbose_name='sub_words')),
            ],
        ),
        migrations.CreateModel(
            name='OurPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=main.models.update_filenamephoto, verbose_name='Picture')),
            ],
        ),
        migrations.AlterModelOptions(
            name='dolzhnost',
            options={},
        ),
        migrations.AddField(
            model_name='people',
            name='dolzhnost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dolzhnost', verbose_name='Dolzhnost'),
        ),
        migrations.AlterField(
            model_name='dolzhnost',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Code'),
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('svg', models.CharField(max_length=105000, verbose_name='Svg')),
                ('framework_categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.frameworkcategories', verbose_name='Framework Categories')),
            ],
        ),
    ]
# Generated by Django 4.1.2 on 2023-01-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seafoodapp', '0021_alter_seafood_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_tempat', models.CharField(max_length=100)),
                ('koordinat', models.CharField(max_length=100)),
            ],
        ),
    ]

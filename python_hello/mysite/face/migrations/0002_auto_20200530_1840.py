# Generated by Django 3.0.6 on 2020-05-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='photo',
            field=models.ImageField(blank=True, upload_to='faces'),
        ),
    ]

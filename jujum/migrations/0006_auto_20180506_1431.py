# Generated by Django 2.0.5 on 2018-05-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jujum', '0005_merge_20180503_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='jujum',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='jujum',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d'),
        ),
    ]

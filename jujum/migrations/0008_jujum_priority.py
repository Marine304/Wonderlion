# Generated by Django 2.0.5 on 2018-05-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jujum', '0007_jujum_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='jujum',
            name='priority',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
# Generated by Django 2.0.4 on 2018-04-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180430_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jujum',
            name='menu',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='nanjang',
            name='menu',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

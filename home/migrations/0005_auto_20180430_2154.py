# Generated by Django 2.0.4 on 2018-04-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180430_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jujum',
            name='menu',
            field=models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='nanjang',
            name='menu',
            field=models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d'),
        ),
    ]

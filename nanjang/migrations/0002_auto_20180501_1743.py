# Generated by Django 2.0.4 on 2018-05-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanjang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nanjang',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='nanjang',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]

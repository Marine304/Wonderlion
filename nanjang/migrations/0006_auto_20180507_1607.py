# Generated by Django 2.0.5 on 2018-05-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanjang', '0005_nanjang_image3'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nanjang',
            options={'ordering': ['priority']},
        ),
        migrations.AddField(
            model_name='nanjang',
            name='priority',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

# Generated by Django 3.2.10 on 2022-07-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='txId',
            field=models.CharField(blank=True, max_length=66, null=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-09-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200929_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_header',
            field=models.TextField(blank=True, null=True),
        ),
    ]

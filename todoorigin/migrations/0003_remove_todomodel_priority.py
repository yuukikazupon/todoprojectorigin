# Generated by Django 3.0.2 on 2020-03-01 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoorigin', '0002_auto_20200301_0544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='PRIORITY',
        ),
    ]

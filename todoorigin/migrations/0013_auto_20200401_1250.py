# Generated by Django 3.0.2 on 2020-04-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoorigin', '0012_auto_20200303_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='title',
            new_name='名前',
        ),
    ]
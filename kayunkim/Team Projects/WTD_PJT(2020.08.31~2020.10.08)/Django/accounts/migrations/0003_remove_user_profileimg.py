# Generated by Django 2.1.15 on 2020-10-06 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_platform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profileImg',
        ),
    ]

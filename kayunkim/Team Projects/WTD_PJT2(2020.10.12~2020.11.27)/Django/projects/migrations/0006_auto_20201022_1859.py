# Generated by Django 2.1.15 on 2020-10-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20201022_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='deadline',
            new_name='end_time',
        ),
        migrations.AddField(
            model_name='task',
            name='manager',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]

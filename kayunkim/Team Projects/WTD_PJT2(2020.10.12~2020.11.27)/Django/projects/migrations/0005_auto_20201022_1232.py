# Generated by Django 2.1.15 on 2020-10-22 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_merge_20201021_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='projects.Keyword'),
        ),
    ]

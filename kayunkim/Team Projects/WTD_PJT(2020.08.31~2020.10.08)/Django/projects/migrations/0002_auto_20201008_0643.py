# Generated by Django 2.1.15 on 2020-10-07 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='project',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
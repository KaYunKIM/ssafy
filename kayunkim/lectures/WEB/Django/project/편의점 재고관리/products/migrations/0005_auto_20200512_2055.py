# Generated by Django 2.1.15 on 2020-05-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200512_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/media/ghost.jpeg', upload_to=''),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20201226_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='paintinglink',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
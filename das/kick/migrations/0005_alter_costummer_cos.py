# Generated by Django 4.1.7 on 2023-03-20 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kick', '0004_rename_is_cos_costummer_cos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costummer',
            name='cos',
            field=models.BooleanField(default=True, null=True),
        ),
    ]

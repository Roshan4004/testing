# Generated by Django 5.0 on 2023-12-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_alldata_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]

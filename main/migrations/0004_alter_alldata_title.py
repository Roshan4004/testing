# Generated by Django 5.0 on 2023-12-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_alldata_added_alter_alldata_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='title',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]

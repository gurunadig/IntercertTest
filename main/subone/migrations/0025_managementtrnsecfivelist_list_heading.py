# Generated by Django 5.0.6 on 2024-09-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0024_managementtrnsecseven_managementtrnsecsevenlist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='managementtrnsecfivelist',
            name='list_heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]

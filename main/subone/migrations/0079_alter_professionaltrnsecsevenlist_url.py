# Generated by Django 5.0.6 on 2024-09-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0078_alter_managementtrnsecsevenlist_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionaltrnsecsevenlist',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

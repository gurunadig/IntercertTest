# Generated by Django 5.0.6 on 2024-10-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0091_trnmainsecthreelistlist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionaltrnsecfive',
            name='section_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]

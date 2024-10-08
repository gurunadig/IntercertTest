# Generated by Django 5.0.6 on 2024-08-27 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0002_aboutuspage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
                ('author', models.TextField()),
                ('robots', models.TextField()),
                ('googlebot', models.TextField()),
                ('language', models.TextField()),
                ('google_site_verification', models.TextField()),
                ('og_url', models.TextField()),
                ('og_type', models.TextField()),
                ('og_title', models.TextField()),
                ('og_desc', models.TextField()),
                ('og_image', models.ImageField(upload_to='og_images/')),
                ('twitter_card', models.TextField()),
                ('twitter_domain', models.TextField()),
                ('twitter_url', models.TextField()),
                ('twitter_title', models.TextField()),
                ('twitter_desc', models.TextField()),
                ('twitter_image', models.ImageField(upload_to='twitter_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Accredition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_title', models.TextField()),
                ('img', models.ImageField(upload_to='accredition/')),
            ],
        ),
        migrations.CreateModel(
            name='ImpartialityPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_title', models.TextField()),
                ('sub_text', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImplementOfIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_title', models.TextField()),
                ('sub_text', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_title', models.TextField()),
                ('sub_text', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QualityPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_title', models.TextField()),
                ('sub_text', models.TextField()),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='quality_policy/')),
                ('text_extra', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WeAreGlobal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_title', models.TextField()),
                ('sub_text', models.TextField()),
                ('img', models.ImageField(upload_to='global/')),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_title', models.TextField()),
                ('sub_text', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_title', models.TextField()),
                ('sub_text', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IOIPList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_text', models.TextField()),
                ('implement_of_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ioip_list', to='subone.implementofip')),
            ],
        ),
        migrations.CreateModel(
            name='OMList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_text', models.TextField()),
                ('our_mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='om_list', to='subone.ourmission')),
            ],
        ),
        migrations.CreateModel(
            name='WUList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('img', models.ImageField(upload_to='why_us/')),
                ('desc', models.TextField()),
                ('why_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wu_list', to='subone.whyus')),
            ],
        ),
        migrations.CreateModel(
            name='WWRList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_text', models.TextField()),
                ('who_we_are', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wwr_list', to='subone.whoweare')),
            ],
        ),
    ]

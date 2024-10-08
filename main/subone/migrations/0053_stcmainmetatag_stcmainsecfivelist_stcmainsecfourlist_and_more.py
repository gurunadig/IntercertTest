# Generated by Django 5.0.6 on 2024-09-09 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0052_ptrnmainpage_ptrnmain_meta'),
    ]

    operations = [
        migrations.CreateModel(
            name='StcMainMetaTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('robots', models.CharField(max_length=255)),
                ('googlebot', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=50)),
                ('google_site_verification', models.CharField(max_length=255)),
                ('og_url', models.CharField(max_length=255)),
                ('og_type', models.CharField(max_length=50)),
                ('og_title', models.CharField(max_length=255)),
                ('og_desc', models.TextField()),
                ('og_image', models.ImageField(upload_to='images/')),
                ('twitter_card', models.CharField(max_length=50)),
                ('twitter_domain', models.CharField(max_length=255)),
                ('twitter_url', models.CharField(max_length=255)),
                ('twitter_title', models.CharField(max_length=255)),
                ('twitter_description', models.TextField()),
                ('twitter_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecFiveList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.TextField()),
                ('list_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecFourList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.TextField()),
                ('list_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecOneList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecSixList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_text', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('desc', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecThreeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.TextField()),
                ('list_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecTwoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.TextField()),
                ('list_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField()),
                ('stcmain_sec_five_list', models.ManyToManyField(related_name='stcmain_sec_five_list', to='subone.stcmainsecfivelist')),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField()),
                ('stcmain_sec_four_list', models.ManyToManyField(related_name='stcmain_sec_four_list', to='subone.stcmainsecfourlist')),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField()),
                ('stcmain_sec_one_list', models.ManyToManyField(related_name='stcmain_sec_one_list', to='subone.stcmainseconelist')),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecSix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField()),
                ('desc', models.TextField()),
                ('stcmain_sec_six_list', models.ManyToManyField(related_name='stcmain_sec_six_list', to='subone.stcmainsecsixlist')),
            ],
        ),
        migrations.CreateModel(
            name='StcMainSecThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField()),
                ('desc', models.TextField()),
                ('stcmain_sec_three_list', models.ManyToManyField(related_name='stcmain_sec_three_list', to='subone.stcmainsecthreelist')),
            ],
        ),
        migrations.CreateModel(
            name='StcMainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=255)),
                ('lp_title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('url_string', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='images/')),
                ('stcmain_meta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stcmain_meta', to='subone.stcmainmetatag')),
                ('stcmain_sec_five', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stcmain_sec_five', to='subone.stcmainsecfive')),
                ('stcmain_sec_four', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stcmain_sec_four', to='subone.stcmainsecfour')),
                ('stcmain_sec_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stcmain_sec_one', to='subone.stcmainsecone')),
                ('stcmain_sec_six', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stcmain_sec_six', to='subone.stcmainsecsix')),
                ('stcmain_sec_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stcmain_sec_three', to='subone.stcmainsecthree')),
                ('stcmain_sec_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stcmain_sec_two', to='subone.stcmainsectwo')),
            ],
        ),
        migrations.AddField(
            model_name='stcmainsectwo',
            name='stcmain_sec_two_list',
            field=models.ManyToManyField(related_name='stcmain_sec_two_list', to='subone.stcmainsectwolist'),
        ),
    ]

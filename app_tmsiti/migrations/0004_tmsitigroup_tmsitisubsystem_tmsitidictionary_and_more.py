# Generated by Django 5.0.6 on 2024-05-15 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tmsiti', '0003_tmsitibuildingreglements_tmsitielecstandards'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMSITIGroup',
            fields=[
                ('abstractbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_tmsiti.abstractbasemodel')),
                ('group_number', models.IntegerField()),
                ('group_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'db_table': 'groups',
            },
            bases=('app_tmsiti.abstractbasemodel',),
        ),
        migrations.CreateModel(
            name='TMSITISubsystem',
            fields=[
                ('abstractbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_tmsiti.abstractbasemodel')),
                ('subsystem_number', models.IntegerField()),
                ('subsystem_title', models.CharField(max_length=255)),
            ],
            bases=('app_tmsiti.abstractbasemodel',),
        ),
        migrations.CreateModel(
            name='TMSITIDictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_name_uz', models.CharField(db_index=True, max_length=255, unique=True)),
                ('word_name_ru', models.CharField(db_index=True, max_length=255, unique=True)),
                ('word_name_en', models.CharField(db_index=True, max_length=255, unique=True)),
                ('word_name_turk', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'TMSITIDictionaries',
                'db_table': 'dictionary',
                'indexes': [models.Index(fields=['word_name_uz'], name='dictionary_word_na_b39b0e_idx'), models.Index(fields=['word_name_ru'], name='dictionary_word_na_7c8df2_idx'), models.Index(fields=['word_name_en'], name='dictionary_word_na_798207_idx'), models.Index(fields=['word_name_turk'], name='dictionary_word_na_3a7f88_idx')],
            },
        ),
        migrations.CreateModel(
            name='TMSITISHNK',
            fields=[
                ('abstractbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_tmsiti.abstractbasemodel')),
                ('SHNK_code', models.CharField(max_length=10)),
                ('SHNK_date', models.CharField(max_length=128)),
                ('SHNK_title', models.CharField(max_length=255)),
                ('SHNK_file_uz', models.FileField(upload_to='shnks/')),
                ('SHNK_file_ru', models.FileField(upload_to='shnks/')),
                ('SHNK_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tmsiti.tmsitigroup')),
            ],
            options={
                'verbose_name_plural': 'SHNKS',
                'db_table': 'shnks',
            },
            bases=('app_tmsiti.abstractbasemodel',),
        ),
        migrations.AddField(
            model_name='tmsitigroup',
            name='group_subsystem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tmsiti.tmsitisubsystem'),
        ),
    ]

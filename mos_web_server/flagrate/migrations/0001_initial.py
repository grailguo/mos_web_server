# Generated by Django 3.2.14 on 2022-07-20 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accio', '0001_initial'),
        ('erecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('activated', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sample_amount', models.DecimalField(decimal_places=6, max_digits=12)),
                ('algorithm_data', models.JSONField(blank=True, default=dict)),
                ('algorithm_parameters', models.JSONField(blank=True, default=dict)),
                ('analysis_parameters', models.JSONField(blank=True, default=dict)),
                ('quant_methods', models.JSONField(blank=True, default=dict)),
                ('config_parameters', models.JSONField(blank=True, default=dict)),
                ('expected_result', models.JSONField(blank=True, default=list)),
            ],
            options={
                'verbose_name': 'case',
                'verbose_name_plural': 'cases',
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('activated', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mrzfile', models.FileField(blank=True, default='', max_length=1024, upload_to='uploads/mrzfiles/%Y/%m/%d/%H/%M/%S/')),
                ('status', models.BooleanField(default=True)),
                ('dbfile', models.FileField(blank=True, default='', max_length=1024, upload_to='uploads/dbfiles/%Y/%m/%d/%H/%M/%S/')),
                ('db_version', models.CharField(blank=True, default='', max_length=16, null=True)),
                ('expected_result', models.JSONField(blank=True, default=list)),
                ('analysis_result', models.JSONField(blank=True, default=list)),
            ],
            options={
                'verbose_name': 'data',
                'verbose_name_plural': 'data',
            },
        ),
        migrations.CreateModel(
            name='DataTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('activated', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'data tag',
                'verbose_name_plural': 'data tags',
            },
        ),
        migrations.CreateModel(
            name='Substance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('activated', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('concentration', models.DecimalField(decimal_places=6, max_digits=12)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substances', to='flagrate.case')),
                ('compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accio.compound')),
                ('conc_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erecto.concunit')),
            ],
            options={
                'verbose_name': 'substance',
                'verbose_name_plural': 'substances',
            },
        ),
    ]

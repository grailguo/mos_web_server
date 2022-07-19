# Generated by Django 3.2.14 on 2022-07-19 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flagrate', '0001_initial'),
        ('reparo', '0001_initial'),
        ('erecto', '0001_initial'),
        ('accio', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='substance',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.organization'),
        ),
        migrations.AddField(
            model_name='datatag',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
        ),
        migrations.AddField(
            model_name='data',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flagrate.case'),
        ),
        migrations.AddField(
            model_name='data',
            name='datatag',
            field=models.ManyToManyField(blank=True, default='', to='flagrate.DataTag'),
        ),
        migrations.AddField(
            model_name='data',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparo.device'),
        ),
        migrations.AddField(
            model_name='data',
            name='neg_compound',
            field=models.ManyToManyField(blank=True, default='', related_name='data_neg_compound', to='accio.Compound'),
        ),
        migrations.AddField(
            model_name='data',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.organization'),
        ),
        migrations.AddField(
            model_name='data',
            name='pos_compound',
            field=models.ManyToManyField(blank=True, default='', related_name='data_pos_compound', to='accio.Compound'),
        ),
        migrations.AddField(
            model_name='case',
            name='cartridge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accio.cartridge'),
        ),
        migrations.AddField(
            model_name='case',
            name='eluent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erecto.eluent'),
        ),
        migrations.AddField(
            model_name='case',
            name='matrix',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erecto.matrix'),
        ),
        migrations.AddField(
            model_name='case',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
        ),
        migrations.AddField(
            model_name='case',
            name='sample_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erecto.unit'),
        ),
    ]
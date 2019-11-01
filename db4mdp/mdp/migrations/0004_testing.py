# Generated by Django 2.0.7 on 2019-06-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdp', '0003_testing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdp',
            name='cartesian',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='categorical',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='complexity',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='complexity_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='dissimilarity',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='linearity',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='locality',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='mdp_fullname',
            field=models.CharField(max_length=500, unique=True, verbose_name='MDP full form'),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='mdp_name',
            field=models.CharField(max_length=500, unique=True, verbose_name='MDP short form'),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='multi_level',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='ne_structures',
            field=models.CharField(max_length=500, verbose_name='Neighbouring Structures'),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='ordinal',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='out_of_core_data',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='reference',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='stability',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='steerability',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='supervision',
            field=models.CharField(max_length=500),
        ),
    ]
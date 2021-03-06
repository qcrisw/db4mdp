# Generated by Django 2.0.7 on 2019-06-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdp', '0002_testing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdp',
            name='cartesian',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='categorical',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='dissimilarity',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='linearity',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='locality',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='multi_level',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='ne_structures',
            field=models.CharField(max_length=100, verbose_name='Neighbouring Structures'),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='ordinal',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='out_of_core_data',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='stability',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='steerability',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdp',
            name='supervision',
            field=models.CharField(max_length=100),
        ),
    ]

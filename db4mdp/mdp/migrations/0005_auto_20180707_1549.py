# Generated by Django 2.0.7 on 2018-07-07 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdp', '0004_languages_r'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrichment',
            fields=[
                ('enrichment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('enrichment_name', models.CharField(max_length=100)),
                ('enrichment_type', models.CharField(max_length=100)),
                ('references_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QualityMeasure',
            fields=[
                ('measure_id', models.IntegerField(primary_key=True, serialize=False)),
                ('measure_name', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('globall', models.CharField(max_length=100)),
                ('dissimilarity', models.CharField(max_length=100)),
                ('correlation', models.CharField(max_length=100)),
                ('probability', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=100)),
                ('geometric', models.CharField(max_length=100)),
                ('set_difference', models.CharField(max_length=100)),
                ('homology', models.CharField(max_length=100)),
                ('rangee', models.CharField(max_length=100)),
                ('best', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.IntegerField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100)),
                ('task_type', models.CharField(max_length=100)),
                ('input_space', models.CharField(max_length=100)),
                ('output_space', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('TS', models.CharField(max_length=100)),
                ('reference_list', models.CharField(max_length=100)),
                ('best_mdp_list', models.CharField(max_length=100)),
                ('task_property', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('variant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mdp_name', models.CharField(max_length=100)),
                ('variants', models.CharField(max_length=100)),
                ('variant_reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='languages',
            name='id',
        ),
        migrations.AlterField(
            model_name='languages',
            name='cplusplus',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='languages',
            name='java',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='languages',
            name='javascript',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='languages',
            name='language_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='languages',
            name='matlab',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='languages',
            name='mdp_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='languages',
            name='python',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='languages',
            name='r',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='languages',
            name='reference_list',
            field=models.CharField(max_length=100),
        ),
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
            name='complexity',
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
            name='mdp_name',
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
            field=models.CharField(max_length=100),
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
            name='reference',
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
        migrations.AddField(
            model_name='variants',
            name='mdp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdp.MDP'),
        ),
        migrations.AddField(
            model_name='task',
            name='mdp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdp.MDP'),
        ),
    ]
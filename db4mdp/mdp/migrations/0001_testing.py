# Generated by Django 2.0.7 on 2019-06-23 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrichment',
            fields=[
                ('enrichment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('enrichment_name', models.CharField(max_length=100, unique=True)),
                ('enrichment_type', models.CharField(max_length=100)),
                ('references_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('language_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mdp_name', models.CharField(max_length=100, unique=True)),
                ('cplusplus', models.CharField(max_length=100, verbose_name='C++')),
                ('java', models.CharField(max_length=100)),
                ('python', models.CharField(max_length=100)),
                ('matlab', models.CharField(max_length=100)),
                ('r', models.CharField(max_length=100)),
                ('javascript', models.CharField(max_length=100)),
                ('reference_list', models.CharField(max_length=300, verbose_name='References')),
            ],
        ),
        migrations.CreateModel(
            name='MDP',
            fields=[
                ('mdp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mdp_name', models.CharField(max_length=100, unique=True, verbose_name='MDP short form')),
                ('mdp_fullname', models.CharField(max_length=100, unique=True, verbose_name='MDP full form')),
                ('reference', models.IntegerField()),
                ('dissimilarity', models.IntegerField()),
                ('ordinal', models.IntegerField()),
                ('cartesian', models.IntegerField()),
                ('ne_structures', models.IntegerField(verbose_name='Neighbouring Structures')),
                ('categorical', models.IntegerField()),
                ('linearity', models.IntegerField()),
                ('supervision', models.IntegerField()),
                ('multi_level', models.IntegerField()),
                ('locality', models.IntegerField()),
                ('steerability', models.IntegerField()),
                ('stability', models.IntegerField()),
                ('out_of_core_data', models.IntegerField()),
                ('complexity', models.CharField(max_length=100)),
                ('complexity_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QualityMeasure',
            fields=[
                ('measure_id', models.IntegerField(primary_key=True, serialize=False)),
                ('measure_name', models.CharField(max_length=100, unique=True)),
                ('local', models.CharField(max_length=100)),
                ('globall', models.CharField(max_length=100, verbose_name='Global')),
                ('dissimilarity', models.CharField(max_length=100)),
                ('correlation', models.CharField(max_length=100)),
                ('probability', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=100)),
                ('geometric', models.CharField(max_length=100)),
                ('set_difference', models.CharField(max_length=100)),
                ('homology', models.CharField(max_length=100)),
                ('rangee', models.CharField(max_length=100, verbose_name='Range')),
                ('best', models.IntegerField(verbose_name='Best MDP')),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.IntegerField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100, unique=True)),
                ('task_type', models.CharField(max_length=100)),
                ('input_space', models.CharField(max_length=100)),
                ('input_space_name', models.CharField(max_length=100)),
                ('output_space', models.CharField(max_length=100)),
                ('output_space_name', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('ts', models.CharField(max_length=100)),
                ('reference_list', models.CharField(max_length=100)),
                ('best_mdp_list', models.CharField(max_length=100)),
                ('task_property', models.CharField(max_length=100)),
                ('mdp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdp.MDP')),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('variant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mdp_name', models.CharField(max_length=100, unique=True)),
                ('variants', models.CharField(max_length=100)),
                ('variant_reference', models.CharField(max_length=100)),
                ('mdp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdp.MDP')),
            ],
        ),
        migrations.AddField(
            model_name='languages',
            name='mdp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdp.MDP'),
        ),
    ]
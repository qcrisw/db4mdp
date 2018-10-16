# Generated by Django 2.0.7 on 2018-07-07 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_id', models.IntegerField()),
                ('mdp_name', models.CharField(max_length=50)),
                ('reference_list', models.CharField(max_length=50)),
                ('cplusplus', models.CharField(max_length=50)),
                ('java', models.CharField(max_length=50)),
                ('python', models.CharField(max_length=50)),
                ('matlab', models.CharField(max_length=50)),
                ('javascript', models.CharField(max_length=50)),
                ('mdp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdp.MDP')),
            ],
        ),
    ]
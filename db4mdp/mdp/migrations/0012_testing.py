# Generated by Django 2.0.7 on 2019-06-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdp', '0011_testing'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='image_name',
            field=models.CharField(default='blank.png', max_length=50, verbose_name='Image Name (New image to be saved in the static directory with the same name)'),
        ),
    ]

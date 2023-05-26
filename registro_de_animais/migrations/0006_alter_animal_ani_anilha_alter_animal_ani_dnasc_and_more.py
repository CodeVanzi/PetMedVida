# Generated by Django 4.2.1 on 2023-05-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_de_animais', '0005_rename_anilha_animal_ani_castr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='ani_anilha',
            field=models.CharField(blank=True, default='não informado', max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_dnasc',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_idade',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_nmchip',
            field=models.CharField(blank=True, default='não informado', max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_obs',
            field=models.CharField(blank=True, default='não informado', max_length=200),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_rga',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_vacinado',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_vermifugado',
            field=models.BooleanField(blank=True),
        ),
    ]
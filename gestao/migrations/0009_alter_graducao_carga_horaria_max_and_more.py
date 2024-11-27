# Generated by Django 5.1.2 on 2024-11-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0008_atividade_usuario_pesquisa_tipo_ensino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graducao',
            name='carga_horaria_max',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='graducao',
            name='carga_horaria_min',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='graducao',
            name='monitoria',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='graducao',
            name='orientacao',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='carga_horaria_max',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='carga_horaria_min',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='curso_pesquisa',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='eventos_pesquisa',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='orientacao',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='posgraduacao',
            name='atividade_mestrado',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='posgraduacao',
            name='aula_mestrado',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='posgraduacao',
            name='carga_horaria_max',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='posgraduacao',
            name='carga_horaria_min',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]

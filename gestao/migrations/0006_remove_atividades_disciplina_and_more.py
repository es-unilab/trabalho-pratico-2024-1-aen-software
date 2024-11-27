# Generated by Django 5.1.2 on 2024-11-01 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0005_pesquisa_remove_orientacaoacademica_atividade_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividades',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='atividades',
            name='modalidade',
        ),
        migrations.RemoveField(
            model_name='atividades',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='data_de_registro',
        ),
        migrations.AlterField(
            model_name='tipoensino',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Ministra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_registro', models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao.disciplina')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Modalidade',
        ),
        migrations.DeleteModel(
            name='Atividades',
        ),
    ]
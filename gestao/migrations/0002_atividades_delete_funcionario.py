# Generated by Django 5.1.2 on 2024-10-14 01:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_registro', models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao.disciplina')),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao.modalidade')),
            ],
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
    ]
# Generated by Django 5.1.2 on 2024-11-03 06:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0007_rename_horario_graducao_aula_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='tipo_ensino',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pesquisa_opcoes', to='gestao.tipoensino'),
        ),
        migrations.AlterField(
            model_name='tipoensino',
            name='atividade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipos_ensino', to='gestao.atividade'),
        ),
    ]
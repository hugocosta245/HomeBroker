# Generated by Django 3.2.3 on 2021-05-20 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiInvest', '0002_conta_taxa_transacao_tipo_transacao_transacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_transacao',
            name='fk_transacao',
        ),
        migrations.AddField(
            model_name='transacao',
            name='fk_tipo_transacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apiInvest.tipo_transacao'),
            preserve_default=False,
        ),
    ]

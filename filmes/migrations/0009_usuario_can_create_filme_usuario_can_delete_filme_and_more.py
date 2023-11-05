# Generated by Django 4.2 on 2023-11-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0008_alter_filme_options_alter_filme_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='can_create_filme',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='can_delete_filme',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='can_update_filme',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$8HlFhjjIUGRQRmTU5xMFX8$OwFnRcXRdKk4kX7ywjxQ6sTCUUKCEDlP2VK3s4QiAI8=', max_length=128),
        ),
    ]

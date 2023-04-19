# Generated by Django 4.2 on 2023-04-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='icono',
        ),
        migrations.AddField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-users', 'Usuarios'), ('lni-cog', 'Engrenagem'), ('lni-mobile', 'mobile'), ('lni-statis-up', 'Grafico'), ('lni-rocket', 'foguete'), ('lni-layer', 'Desingn')], default=1, max_length=100, verbose_name='icone'),
            preserve_default=False,
        ),
    ]
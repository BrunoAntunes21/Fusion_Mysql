# Generated by Django 4.2 on 2023-04-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_servico_icono_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'foguete'), ('lni-cog', 'Engrenagem'), ('lni-mobile', 'mobile'), ('lni-layer', 'Desingn'), ('lni-statis-up', 'Grafico'), ('lni-users', 'Usuarios')], max_length=100, verbose_name='icone'),
        ),
    ]

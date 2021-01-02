# Generated by Django 2.0 on 2021-01-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0020_auto_20210101_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.PositiveIntegerField(choices=[(0, '--------------'), (1, 'IDENTITY'), (2, 'BORDA'), (3, 'HONDT'), (4, 'EQUALITY'), (5, 'SAINTE_LAGUE'), (6, 'DROOP'), (7, 'IMPERIALI'), (8, 'HARE')], default='0'),
        ),
    ]

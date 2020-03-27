# Generated by Django 3.0.4 on 2020-03-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('split_bill', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='split_num',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='full_bill',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]

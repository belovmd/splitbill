# Generated by Django 3.0.4 on 2020-04-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('split_bill', '0005_auto_20200418_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='summa',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
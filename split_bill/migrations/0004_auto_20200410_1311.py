# Generated by Django 3.0.4 on 2020-04-10 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('split_bill', '0003_auto_20200407_1226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'ordering': ['-date_time']},
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='date',
            new_name='date_time',
        ),
    ]

# Generated by Django 2.1.1 on 2018-10-04 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aguardando', '0004_auto_20181004_0940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chegando',
            options={'ordering': ['produto', 'container']},
        ),
    ]

# Generated by Django 4.2.13 on 2024-11-10 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_productmaterial_advantages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksection',
            name='important',
            field=models.BooleanField(default=False, verbose_name='Important'),
        ),
    ]

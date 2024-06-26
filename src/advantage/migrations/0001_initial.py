# Generated by Django 4.2.13 on 2024-06-26 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirmAdvantage',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Advantage id')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('paragraph', models.TextField(verbose_name='Main paragraph')),
            ],
            options={
                'verbose_name': 'Firm advantage',
                'verbose_name_plural': 'Firm advantages',
                'db_table': 'firm_advantages',
            },
        ),
        migrations.CreateModel(
            name='MaterialAdvantage',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Advantage id')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('paragraph', models.TextField(verbose_name='Main paragraph')),
            ],
            options={
                'verbose_name': 'Material advantage',
                'verbose_name_plural': 'Material advantages',
                'db_table': 'material_advantages',
            },
        ),
    ]

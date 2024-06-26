# Generated by Django 4.2.13 on 2024-06-26 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Item id')),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='image.doublesidedimage', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Portfolio item',
                'verbose_name_plural': 'Portfolio items',
                'db_table': 'portfolio_list',
            },
        ),
    ]

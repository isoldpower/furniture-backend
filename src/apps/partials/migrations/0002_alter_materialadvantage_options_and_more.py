# Generated by Django 4.2.13 on 2024-06-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialadvantage',
            options={'verbose_name': 'Material advantage', 'verbose_name_plural': 'Material advantages'},
        ),
        migrations.AlterField(
            model_name='doublesidedimage',
            name='low_src',
            field=models.ImageField(upload_to='images/', verbose_name='Low resolution'),
        ),
        migrations.AlterField(
            model_name='doublesidedimage',
            name='src',
            field=models.ImageField(upload_to='images/', verbose_name='High resolution'),
        ),
    ]
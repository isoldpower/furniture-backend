# Generated by Django 4.2.13 on 2024-11-10 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_stocksection_important'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocksection',
            old_name='important',
            new_name='visible_in_header',
        ),
        migrations.AddField(
            model_name='stocksection',
            name='visible_in_preview',
            field=models.BooleanField(default=False, verbose_name='Visible in preview'),
        ),
    ]

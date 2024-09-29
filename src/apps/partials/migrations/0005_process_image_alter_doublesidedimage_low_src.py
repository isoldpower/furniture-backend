# Generated by Django 4.2.13 on 2024-09-29 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partials', '0004_abstractadvantage_process_delete_firmadvantage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partials.doublesidedimage', verbose_name='Process image'),
        ),
        migrations.AlterField(
            model_name='doublesidedimage',
            name='low_src',
            field=models.ImageField(editable=False, upload_to='thumbnails/', verbose_name='Low resolution'),
        ),
    ]
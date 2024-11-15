# Generated by Django 4.2.13 on 2024-06-28 18:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCallRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Request id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('name', models.CharField(max_length=255, verbose_name='Client name')),
                ('phone_number', models.CharField(max_length=31, unique=True, verbose_name='Phone number')),
                ('email_address', models.CharField(max_length=255, unique=True, verbose_name='Email address')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.stockproduct', verbose_name='Product of interest')),
            ],
            options={
                'verbose_name': 'Phone call',
                'verbose_name_plural': 'Phone calls',
                'db_table': 'phone_calls',
            },
        ),
    ]

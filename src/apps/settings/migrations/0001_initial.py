# Generated by Django 4.2.13 on 2024-06-28 18:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SectionedSettings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Settings id')),
                ('verbose_name', models.CharField(default='Название', verbose_name='Name')),
                ('key', models.CharField(default='FIELD_KEY', max_length=255, unique=True, verbose_name='Unique key')),
                ('value', models.TextField(default='', verbose_name='Settings value')),
                ('section', models.CharField(choices=[('global', 'Global'), ('home_hero', 'Hero'), ('home_quote', 'Quote'), ('about_page', 'About'), ('footer_address', 'Address'), ('catalog_page', 'Catalog'), ('socials_links', 'Links')], default='global', editable=False, verbose_name='Related section')),
            ],
            options={
                'ordering': ['verbose_name'],
            },
        ),
        migrations.CreateModel(
            name='AboutSettings',
            fields=[
                ('sectionedsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.sectionedsettings')),
            ],
            options={
                'verbose_name': 'About Settings',
                'verbose_name_plural': 'About Settings',
            },
            bases=('settings.sectionedsettings',),
        ),
        migrations.CreateModel(
            name='AddressSettings',
            fields=[
                ('sectionedsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.sectionedsettings')),
            ],
            options={
                'verbose_name': 'Address Settings',
                'verbose_name_plural': 'Address Settings',
            },
            bases=('settings.sectionedsettings',),
        ),
        migrations.CreateModel(
            name='CatalogSettings',
            fields=[
                ('sectionedsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.sectionedsettings')),
            ],
            options={
                'verbose_name': 'Catalog Settings',
                'verbose_name_plural': 'Catalog Settings',
            },
            bases=('settings.sectionedsettings',),
        ),
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('sectionedsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.sectionedsettings')),
            ],
            options={
                'verbose_name': 'Global Settings',
                'verbose_name_plural': 'Global Settings',
            },
            bases=('settings.sectionedsettings',),
        ),
        migrations.CreateModel(
            name='HeroSettings',
            fields=[
                ('sectionedsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.sectionedsettings')),
            ],
            options={
                'verbose_name': 'Hero Settings',
                'verbose_name_plural': 'Hero Settings',
            },
            bases=('settings.sectionedsettings',),
        ),
        migrations.CreateModel(
            name='LinksSettings',
            fields=[
                ('sectionedsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.sectionedsettings')),
            ],
            options={
                'verbose_name': 'Links Settings',
                'verbose_name_plural': 'Links Settings',
            },
            bases=('settings.sectionedsettings',),
        ),
        migrations.CreateModel(
            name='QuoteSettings',
            fields=[
                ('sectionedsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.sectionedsettings')),
            ],
            options={
                'verbose_name': 'Quote Settings',
                'verbose_name_plural': 'Quote Settings',
            },
            bases=('settings.sectionedsettings',),
        ),
    ]

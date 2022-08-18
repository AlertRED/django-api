# Generated by Django 4.0.4 on 2022-08-18 14:32

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Дата обновления')),
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('source_name', models.CharField(max_length=32, unique=True, verbose_name='Название ресурса')),
                ('contact_value', models.CharField(max_length=32, verbose_name='Значение контакта')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-18 10:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RaiseTicketForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('subject', models.CharField(max_length=200)),
                ('issue', models.CharField(max_length=1900)),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed')], max_length=7)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tickets_raiseticketform',
            },
        ),
    ]
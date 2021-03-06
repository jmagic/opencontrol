# Generated by Django 3.1 on 2020-08-11 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('is_online', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('state', models.BooleanField(default=False)),
                ('set_on', models.BooleanField(default=False)),
                ('set_off', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plankowner.device')),
            ],
        ),
        migrations.CreateModel(
            name='PanelStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('talents', models.ManyToManyField(to='plankowner.Talent')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('authorized', models.BooleanField(default=False)),
                ('is_online', models.BooleanField(default=False)),
                ('watchdog', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='plankowner.driver'),
        ),
    ]

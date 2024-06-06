# Generated by Django 5.0.6 on 2024-06-06 11:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_enabled', models.BooleanField(default=False)),
                ('discord_enabled', models.BooleanField(default=False)),
                ('facebook_enabled', models.BooleanField(default=False)),
                ('computer_enabled', models.BooleanField(default=False)),
                ('rh_access_token', models.CharField(blank=True, max_length=255, null=True)),
                ('fb_email', models.CharField(blank=True, max_length=255, null=True)),
                ('fb_pass', models.CharField(blank=True, max_length=255, null=True)),
                ('dc_email', models.CharField(blank=True, max_length=255, null=True)),
                ('dc_pass', models.CharField(blank=True, max_length=255, null=True)),
                ('groq_api_key', models.CharField(blank=True, max_length=255, null=True)),
                ('text_sid', models.CharField(blank=True, max_length=255, null=True)),
                ('text_username', models.CharField(blank=True, max_length=255, null=True)),
                ('text_csrf', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_entries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
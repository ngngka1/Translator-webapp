# Generated by Django 5.0.2 on 2024-02-29 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('search_time', models.DateField(default=datetime.date.today)),
                ('partOfSpeech', models.TextField(default='')),
                ('definition', models.TextField(default='')),
                ('synonyms', models.TextField(default='')),
                ('antonyms', models.TextField(default='')),
            ],
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-01 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='semres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=20)),
                ('pinno', models.CharField(max_length=20)),
                ('marks', models.IntegerField()),
                ('college', models.CharField(max_length=20)),
            ],
        ),
    ]

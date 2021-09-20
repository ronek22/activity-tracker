# Generated by Django 3.2.7 on 2021-09-03 11:43

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
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Running', 'Running'), ('Cycling', 'Cycling'), ('Hiking', 'Hiking')], default='Running', max_length=7, verbose_name='Activity Type')),
                ('effort', models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Max Effort', 'Max Effort')], default='Easy', max_length=20, verbose_name='Activity Effort')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('duration', models.DurationField()),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='updated_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'activities',
            },
        ),
    ]
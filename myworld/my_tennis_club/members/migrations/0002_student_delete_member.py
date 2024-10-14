# Generated by Django 5.0.6 on 2024-05-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True)),
                ('college_name', models.CharField(max_length=255)),
                ('year_of_study', models.CharField(max_length=20)),
                ('academic_progress', models.JSONField(default=list)),
                ('result', models.CharField(max_length=50)),
                ('exercise_time', models.CharField(max_length=50)),
                ('sleep_time', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=100)),
                ('learned_from_friend', models.TextField()),
                ('extra_activity', models.TextField()),
                ('req_for_3_months', models.JSONField(default=list)),
                ('book_read', models.TextField()),
                ('ladder_status', models.CharField(max_length=50)),
                ('book_review', models.TextField()),
                ('essay', models.TextField()),
                ('action_for_next_month', models.TextField()),
                ('difficulties', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]

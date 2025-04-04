# Generated by Django 3.2.25 on 2025-03-25 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('grade_level', models.CharField(blank=True, max_length=50, null=True)),
                ('academic_year', models.CharField(blank=True, max_length=20, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='core.school')),
            ],
            options={
                'verbose_name_plural': 'School Classes',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('parent_name', models.CharField(blank=True, max_length=200, null=True)),
                ('parent_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='core.school')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='core.schoolclass')),
            ],
        ),
    ]

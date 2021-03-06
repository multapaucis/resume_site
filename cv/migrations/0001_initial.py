# Generated by Django 2.1.1 on 2018-10-02 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
                ('date_started', models.DateField()),
                ('date_finished', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_started', models.DateField()),
                ('date_finished', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cv.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
                ('skill_type', models.CharField(max_length=200)),
            ],
        ),
    ]

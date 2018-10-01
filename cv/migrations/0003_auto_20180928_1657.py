# Generated by Django 2.1.1 on 2018-09-28 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20180928_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='id',
        ),
        migrations.AlterField(
            model_name='job',
            name='date_finished',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_started',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]

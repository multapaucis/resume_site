# Generated by Django 2.1.1 on 2018-10-06 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20181006_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='stype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cv.SkillType'),
        ),
    ]

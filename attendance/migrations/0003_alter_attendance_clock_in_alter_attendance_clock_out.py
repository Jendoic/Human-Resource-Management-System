# Generated by Django 5.1.2 on 2024-10-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='clock_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='clock_out',
            field=models.DateTimeField(),
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_auto_20210430_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry_details',
            name='demo_lecture_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inquiry_details',
            name='demo_lecture_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
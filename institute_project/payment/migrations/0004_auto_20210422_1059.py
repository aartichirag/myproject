# Generated by Django 3.1.7 on 2021-04-22 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20210422_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='bank_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='payment_details',
            name='branch_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='payment_details',
            name='chaque_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

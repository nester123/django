# Generated by Django 5.1.1 on 2024-09-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

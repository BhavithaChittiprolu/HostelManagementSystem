# Generated by Django 3.2.18 on 2023-03-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0023_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='receipt',
            field=models.FileField(null=True, upload_to='media/expenses'),
        ),
    ]
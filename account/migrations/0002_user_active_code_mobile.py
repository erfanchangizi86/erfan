# Generated by Django 5.0.6 on 2024-07-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active_code_mobile',
            field=models.CharField(default=1, max_length=5, unique=True),
            preserve_default=False,
        ),
    ]
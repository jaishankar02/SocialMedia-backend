# Generated by Django 4.1.1 on 2023-07-07 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='feeduser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile'),
        ),
    ]

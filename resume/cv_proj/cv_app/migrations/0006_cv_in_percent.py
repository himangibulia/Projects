# Generated by Django 4.2.4 on 2023-09-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0005_remove_cv_in_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='in_percent',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

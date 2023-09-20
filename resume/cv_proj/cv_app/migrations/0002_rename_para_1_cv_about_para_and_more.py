# Generated by Django 4.2.4 on 2023-09-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='para_1',
            new_name='about_para',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='percent_1',
            new_name='percentage',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='percent_2',
            new_name='skill_in_percent',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='interest_1',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='interest_2',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='interest_3',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='interest_4',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='language_1',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='language_2',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='para_2',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='percent_3',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='percent_4',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='percent_5',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='percent_6',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='percentage_1',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='percentage_2',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='skill_1',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='skill_2',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='skill_3',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='skill_4',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='skill_5',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='skill_6',
        ),
        migrations.AddField(
            model_name='cv',
            name='interest',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='language',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='skill',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
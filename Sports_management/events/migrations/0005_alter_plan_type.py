# Generated by Django 5.1.4 on 2025-01-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_plan_command_alter_plan_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='type',
            field=models.CharField(choices=[('Inter_Batallion', 'Inter_Batallion'), ('Inter_Division', 'Inter_Division'), ('Inter_Corps', 'Inter_Corps'), ('Inter_Command', 'Inter_Command')], max_length=200),
        ),
    ]

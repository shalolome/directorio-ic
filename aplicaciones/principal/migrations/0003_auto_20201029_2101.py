# Generated by Django 3.1.2 on 2020-10-30 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_persona_experiencia_laboral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='identificacion',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
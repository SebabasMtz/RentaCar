# Generated by Django 5.1.2 on 2024-10-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=25)),
                ('modelo', models.CharField(max_length=25)),
                ('año', models.IntegerField()),
                ('precio_por_dia', models.DecimalField(decimal_places=2, max_digits=4)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]
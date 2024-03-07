# Generated by Django 5.0.2 on 2024-03-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0010_remove_doctor_days_doctor_days_in_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='days_in_hospital',
        ),
        migrations.AddField(
            model_name='doctor',
            name='days_in_hospital',
            field=models.ManyToManyField(to='Base.day'),
        ),
    ]
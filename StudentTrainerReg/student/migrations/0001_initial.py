# Generated by Django 3.1.7 on 2021-04-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudComplete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=150)),
                ('year', models.FloatField()),
                ('percentage', models.IntegerField()),
                ('course', models.CharField(max_length=100)),
                ('mode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
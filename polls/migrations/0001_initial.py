# Generated by Django 2.0.5 on 2018-06-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('cdate', models.DateTimeField()),
                ('pwd', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
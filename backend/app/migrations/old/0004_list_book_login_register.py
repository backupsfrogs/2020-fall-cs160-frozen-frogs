# Generated by Django 3.1.1 on 2020-09-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200926_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('isbn', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=300)),
                ('class_used', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sjsu_id', models.CharField(max_length=9)),
                ('sjsu_pw', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sjsu_id', models.CharField(max_length=9)),
                ('sjsu_pw', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-02 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201001_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.list_book', verbose_name='BookForSale'),
        ),
    ]

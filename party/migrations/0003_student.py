# Generated by Django 4.1.3 on 2022-11-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_itemmodel_alter_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.2.28 on 2022-12-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test34',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.BigIntegerField()),
            ],
        ),
    ]
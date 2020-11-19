# Generated by Django 3.1.3 on 2020-11-18 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('days', models.IntegerField()),
                ('hours', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('seconds', models.IntegerField()),
            ],
        ),
    ]

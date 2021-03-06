# Generated by Django 2.0.7 on 2019-09-17 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190918_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_id', models.CharField(max_length=15)),
                ('med_name', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('is_available', models.BooleanField(default=False)),
                ('order_id', models.CharField(max_length=15)),
            ],
        ),
    ]

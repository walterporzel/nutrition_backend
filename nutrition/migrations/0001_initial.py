# Generated by Django 2.2.6 on 2019-10-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('serving_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('serving_size_unit', models.CharField(max_length=100)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carbs', models.DecimalField(decimal_places=2, max_digits=5)),
                ('protien', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

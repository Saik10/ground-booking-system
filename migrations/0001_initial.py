# Generated by Django 3.2.7 on 2022-05-24 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groundapp', '0002_alter_owner_timings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Ground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=100)),
                ('ground_type', models.CharField(max_length=200)),
                ('ground_images', models.ImageField(upload_to='')),
                ('timings', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groundapp.owner')),
            ],
            options={
                'db_table': 'add_ground',
            },
        ),
    ]
# Generated by Django 2.1.4 on 2019-03-04 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer_details',
            fields=[
                ('farmer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='rahul', max_length=400)),
                ('last_name', models.CharField(default='moorthy', max_length=400)),
                ('address', models.CharField(default='b302', max_length=100)),
                ('district', models.CharField(default='pune', max_length=100)),
                ('state', models.CharField(default='Maharashtra', max_length=100)),
                ('age', models.IntegerField(default=20)),
                ('farmer_reg_id', models.CharField(default='abcd', max_length=100)),
                ('phone_no', models.CharField(default='8805979825', max_length=100)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='rent_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.IntegerField()),
                ('equipment_quantity', models.IntegerField()),
                ('status_bit', models.IntegerField(blank=True)),
                ('farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.farmer_details')),
            ],
        ),
    ]

# Generated by Django 3.1 on 2020-09-07 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200907_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='side',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.ordersidetype'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_in_force',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.timeinforce'),
        ),
        migrations.AlterField(
            model_name='ordersidetype',
            name='symbol',
            field=models.CharField(help_text='The symbol of the type', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='ordertype',
            name='symbol',
            field=models.CharField(help_text='The symbol of the order type', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='timeinforce',
            name='symbol',
            field=models.CharField(help_text='GTK, IOC, or FOK', max_length=6, unique=True),
        ),
    ]
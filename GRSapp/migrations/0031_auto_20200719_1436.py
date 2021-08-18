# Generated by Django 3.0.8 on 2020-07-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRSapp', '0030_auto_20200719_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='hearts',
            field=models.IntegerField(default=32),
        ),
        migrations.AlterField(
            model_name='camera',
            name='rating',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='camerareview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fridgereview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='headset',
            name='hearts',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='headset',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='headsetreview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='hearts',
            field=models.IntegerField(default=27),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='rating',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='kettlereview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='laptopreview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mobilereview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='hearts',
            field=models.IntegerField(default=22),
        ),
        migrations.AlterField(
            model_name='powerbank',
            name='hearts',
            field=models.IntegerField(default=24),
        ),
        migrations.AlterField(
            model_name='powerbank',
            name='rating',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='powerbankreview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='hearts',
            field=models.IntegerField(default=13),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='rating',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='television',
            name='hearts',
            field=models.IntegerField(default=28),
        ),
        migrations.AlterField(
            model_name='television',
            name='rating',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='televisionreview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='washingmachine',
            name='hearts',
            field=models.IntegerField(default=35),
        ),
        migrations.AlterField(
            model_name='washingmachine',
            name='rating',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='washmanchinereview',
            name='userid',
            field=models.CharField(max_length=50),
        ),
    ]

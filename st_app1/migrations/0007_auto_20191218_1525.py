# Generated by Django 2.1.5 on 2019-12-18 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('st_app1', '0006_auto_20191218_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='episode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prod_episode', to='st_app1.Episode'),
        ),
        migrations.AddField(
            model_name='product',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prod_season', to='st_app1.Season'),
        ),
    ]
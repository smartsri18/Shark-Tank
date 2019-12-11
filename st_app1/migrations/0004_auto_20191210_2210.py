# Generated by Django 2.1.5 on 2019-12-10 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('st_app1', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company',
            new_name='company_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='company_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='st_app1.Company'),
        ),
    ]
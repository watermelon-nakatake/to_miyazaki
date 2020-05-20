# Generated by Django 3.0.6 on 2020-05-20 03:10

from django.db import migrations, models
import info_edit.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('info_edit', '0007_auto_20200520_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuimage',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='restaurantimage',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='menuimage',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=info_edit.models.make_menu_upload_path),
        ),
    ]

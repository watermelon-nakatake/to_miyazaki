# Generated by Django 3.0.6 on 2020-05-19 05:56

from django.db import migrations
import info_edit.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('info_edit', '0004_auto_20200519_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantimage',
            name='original_image',
        ),
        migrations.AlterField(
            model_name='restaurantimage',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=info_edit.models.make_upload_path),
        ),
    ]
# Generated by Django 3.1.3 on 2020-11-26 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_menu_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='menu_id',
            new_name='menu',
        ),
    ]

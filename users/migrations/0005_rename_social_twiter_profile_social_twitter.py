# Generated by Django 3.2.4 on 2022-12-29 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20221229_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_twiter',
            new_name='social_twitter',
        ),
    ]

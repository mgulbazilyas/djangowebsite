# Generated by Django 2.2.3 on 2019-07-26 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0002_auto_20190726_0522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pics',
            new_name='picture',
        ),
    ]

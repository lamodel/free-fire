# Generated by Django 3.2.3 on 2021-05-23 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diamond',
            old_name='emamob',
            new_name='email',
        ),
    ]

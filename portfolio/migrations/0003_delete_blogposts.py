# Generated by Django 3.0.3 on 2020-02-18 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blogposts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blogposts',
        ),
    ]

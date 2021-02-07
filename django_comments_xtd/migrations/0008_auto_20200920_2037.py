# Generated by Django 3.0.1 on 2020-09-20 18:37
from django.core.management import call_command
from django.db import migrations


def populate_nested_count(*args):
    call_command('initialize_nested_count')


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments_xtd', '0007_xtdcomment_nested_count'),
    ]

    operations = [
        migrations.RunPython(populate_nested_count,
                            reverse_code=migrations.RunPython.noop)
    ]
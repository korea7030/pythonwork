# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-11 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_wordEx', '0002_auto_20181011_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketmain',
            old_name='sender_customer',
            new_name='sender_customer_id',
        ),
    ]
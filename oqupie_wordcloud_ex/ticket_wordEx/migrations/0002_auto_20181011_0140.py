# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-11 01:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_wordEx', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brandmain',
            old_name='oniondesk',
            new_name='oniondesk_id',
        ),
        migrations.RenameField(
            model_name='ticketmain',
            old_name='assign_member',
            new_name='assign_member_id',
        ),
        migrations.RenameField(
            model_name='ticketmain',
            old_name='brand_facebook',
            new_name='brand_facebook_id',
        ),
        migrations.RenameField(
            model_name='ticketmain',
            old_name='charge_member',
            new_name='charge_member_id',
        ),
        migrations.RenameField(
            model_name='ticketmain',
            old_name='charge_team',
            new_name='charge_team_id',
        ),
    ]

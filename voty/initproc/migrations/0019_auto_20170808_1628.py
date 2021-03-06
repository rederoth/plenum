# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-08 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
from django.contrib.auth import get_user_model
import django.db.models.deletion

from voty.initproc.globals import STATES

def migrate_eligible_voters_count(apps, schema_editor):
    # Let's set the eligable voters past initiation
    Initiative = apps.get_model('initproc', 'Initiative')
    User = get_user_model()
    for init in Initiative.objects.filter(state__in=[STATES.COMPLETED, STATES.ACCEPTED, STATES.REJECTED]):
        if init.was_closed_at:
            init.eligible_voters = User.objects.filter(date_joined__lte=init.was_closed_at).count()
            init.save()


class Migration(migrations.Migration):

    dependencies = [
        ('initproc', '0018_auto_20170808_1628'),
    ]

    operations = [
        migrations.RunPython(migrate_eligible_voters_count, reverse_code=migrations.RunPython.noop),
    ]

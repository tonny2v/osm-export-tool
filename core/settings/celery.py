# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from celery.schedules import crontab

from .contrib import *  # NOQA

# Celery config
CELERY_TRACK_STARTED = True

"""
 IMPORTANT

 Don't propagate exceptions in the celery chord header to the finalize task.
 If exceptions are thrown in the chord header then allow the
 finalize task to collect the results and update the overall run state.

 @see tasks.task_runners.ExportTaskRunner#161

"""
CELERY_CHORD_PROPAGATES = False

# configure periodic task
CELERYBEAT_SCHEDULE = {
}

BROKER_URL = os.environ.get('BROKER_URL', 'amqp://guest:guest@localhost:5672//')
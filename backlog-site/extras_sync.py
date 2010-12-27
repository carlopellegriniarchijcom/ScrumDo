#!/usr/bin/env python
import sys
from datetime import date, timedelta

from os.path import abspath, dirname, join

try:
    import pinax
except ImportError:
    sys.stderr.write("Error: Can't import Pinax. Make sure you are in a virtual environment that has Pinax installed or create one with pinax-boot.py.\n")
    sys.exit(1)

from django.conf import settings
from django.core.management import setup_environ, execute_from_command_line

try:
    import settings as settings_mod # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

# setup the environment before we start accessing things in the settings.
setup_environ(settings_mod)

sys.path.insert(0, join(settings.PINAX_ROOT, "apps"))
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

from apps.projects.models import Project, Iteration, Story, PointsLog
from apps.extras.models import ProjectExtraMapping, SyncronizationQueue
from apps.extras.manager import manager


def main():
  queue = SyncronizationQueue.objects.all()
  for queueItem in queue:
    try:
      project = queueItem.project
      story = queueItem.story
      action = queueItem.action
      extra_slug = queueItem.extra_slug
      action = queueItem.action
      queueItem.delete()
      extra = manager.getExtra( extra_slug )
      if action == SyncronizationQueue.ACTION_SYNC_REMOTE:
        extra.pullProject(project)        
      elif action == SyncronizationQueue.ACTION_STORY_UPDATED:
      
      
      
      ACTION_SYNC_REMOTE = 1
      ACTION_STORY_UPDATED = 2
      ACTION_STORY_DELETED = 3
      ACTION_STORY_CREATED = 4
      ACTION_PROJECT_UPLOAD = 5
    except:
      pass
    
    


if __name__ == "__main__":
    main()

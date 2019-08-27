#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mineral_catalog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # --- Nose/Coverage limitation Workaround ---
    # Models are imported by the app configuration process. Therefore, by
    # default, running manage.py test will report incorrect model coverage
    # information since the models are imported before the test command is
    # executed.
    # Note, this is only a problem if manage.py is responsible for generating
    # coverage (i.e., execute `python manage.py test` and use the test config
    # from `settings.py`). In contrast `coverage run manage.py test` works
    # fine since the coverage tracking begins before manage.py starts.
    # Thus this workaround is only necessary if we are using Nose and manage.py 
    # to generate the coverage report
    # See: https://github.com/jazzband/django-nose/issues/180
    is_testing = 'test' in sys.argv

    if is_testing:
        import coverage
        cov = coverage.coverage()
        cov.erase()
        cov.start()
    # ---End Workaround
    
    execute_from_command_line(sys.argv)

    # --- Nose/Coverage limitation Workaround ---
    if is_testing:
        cov.stop()
        cov.save()
        cov.report()
    # ---

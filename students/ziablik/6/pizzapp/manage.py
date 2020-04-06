# -*- coding: utf-8 -*-

"""Django's command-line utility for administrative tasks."""
import os
import sys

import django

from django.conf import settings   # noqa: I001

settings.configure()


def main():
    """Main function for manage.py."""
    settings.DEBUG = True
    settings.DJANGO_SETTINGS_MODULE = 'pizzapp.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzapp.settings')
    django.setup()
    try:
        from django.core.management import execute_from_command_line  # noqa: WPS433, E501
    except ImportError as exc:
        raise ImportError(
            'Couldnt import Django. Are you sure its installed and ' +
            'available on your PYTHONPATH environment variable? Did you ' +
            'forget to activate a virtual environment?',
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

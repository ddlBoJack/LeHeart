#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""
Django Document in Using Django -- Django settings
either configure or settings.py (DJANGO_SETTINGS_MODULE)
"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Lexin_Site.settings')
    # 在系统变量（快照）中加入参数对应的键值对;选定这个项目用的什么settings django的一个特点就是弱耦合
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

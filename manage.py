import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Disable autoreload if running inside PyInstaller
    if hasattr(sys, '_MEIPASS'):
        # Replace 'runserver' with '--noreload'
        sys.argv = [arg for arg in sys.argv if arg != 'runserver']
        sys.argv.extend(['runserver', '--noreload'])

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

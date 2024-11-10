"""
Python 3.13 REPL for Django.

To use, put this in a management/commands/shell.py in an installed Django app.

This relies on the undocumented _pyrepl module and may break in future Python versions.
"""

from django.core.management.commands.shell import Command as BaseShellCommand


class Command(BaseShellCommand):
    shells = ["ipython", "bpython", "pyrepl", "python"]

    def pyrepl(self, options):
        from _pyrepl.main import interactive_console

        print("loaded new shell code")
        interactive_console()

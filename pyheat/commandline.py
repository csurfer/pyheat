#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
pyheat as a command
~~~~~~~~~~~~~~~~~~

   Usage:

   >>> pyheat --help
   usage: pyheat [-h] [--pyfile PYFILE]

    optional arguments:
      -h, --help       show this help message and exit
      --pyfile PYFILE  File to be profiled.

   >>> pyheat --pyfile <filename>
   # Displays the heatmap for the file.
"""

import argparse

from .pyheat import PyHeat


def main():
    """Starting point for the program execution."""
    # Create command line parser.
    parser = argparse.ArgumentParser()
    # Adding command line arguments.
    parser.add_argument('--pyfile', help='File to be profiled.', default=None)
    # Parse command line arguments.
    arguments = parser.parse_args()

    if arguments.pyfile is not None:
        # Core functionality.
        pyheat = PyHeat(arguments.pyfile)
        pyheat.create_heatmap()
        pyheat.show_heatmap()
        pyheat.close_heatmap()
    else:
        # Print command help
        parser.print_help()


if __name__ == '__main__':
    main()

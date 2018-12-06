#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
pyheat as a command
~~~~~~~~~~~~~~~~~~

Usage:

    >>> pyheat --help
    usage: pyheat [-h] [-o OUT] pyfile

    positional arguments:
    pyfile             Python file to be profiled

    optional arguments:
    -h, --help         show this help message and exit
    -o OUT, --out OUT  Output file

    >>> pyheat <filename>
    # Displays the heatmap for the file.

    >>> pyheat <filename> --out myimage.png
    # Saves the heatmap as an image in file myimage.png
"""

import argparse

from .pyheat import PyHeat


def main():
    """Starting point for the program execution."""
    # Create command line parser.
    parser = argparse.ArgumentParser()
    # Adding command line arguments.
    parser.add_argument("-o", "--out", help="Output file", default=None)
    parser.add_argument(
        "pyfile", help="Python file to be profiled", default=None
    )
    # Parse command line arguments.
    arguments = parser.parse_args()
    if arguments.pyfile is not None:
        # Core functionality.
        pyheat = PyHeat(arguments.pyfile)
        pyheat.create_heatmap()
        pyheat.show_heatmap(output_file=arguments.out, enable_scroll=True)
        pyheat.close_heatmap()
    else:
        # Print command help
        parser.print_help()


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

#                  __               __
#     ____  __  __/ /_  ___  ____ _/ /_
#    / __ \/ / / / __ \/ _ \/ __ `/ __/
#   / /_/ / /_/ / / / /  __/ /_/ / /_
#  / .___/\__, /_/ /_/\___/\__,_/\__/
# /_/    /____/

"""
pyheat module
~~~~~~~~~~~~~

Usage of PyHeat class:

    >>> from pyheat import PyHeat
    >>> ph = PyHeat(<file_path>)
    >>> ph.create_heatmap()
    >>> ph.show_heatmap()

:copyright: (c) 2017 by Vishwas B Sharma.
:license: MIT, see LICENSE for more details.
"""

__title__ = 'pyheat'
__version__ = '0.0.1'
__author__ = 'Vishwas B Sharma'
__author_email__ = 'sharma.vishwas88@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 Vishwas B Sharma'

from .pyheat import PyHeat

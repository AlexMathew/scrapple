"""
Scrapple
========

Scrapple is a framework for building and running web scrapers/crawlers according to \
key-value pair based configuration files.

:copyright: 2015 Alex Mathew, see AUTHORS for more details
:license: MIT, see LICENSE for more details
"""

from __future__ import print_function

__author__ = "Alex Mathew, and Harish Balakrishnan"
__copyright__ = "Copyright 2015, Alex Mathew"
__credits__ = ["Alex Mathew", "Harish Balakrishnan"]
__license__ = "MIT"
__version__ = "0.1"
__status__ = "Development"
__maintainer__ = "Alex Mathew"
__email__ = "alexmathew003@gmail.com"

__all__ = ["__version__", "command"]

import sys
if sys.version_info < (2, 7):
	print("Scrapple %s requires atleast Python 2.7" % __version__)
	sys.exit(1)
del sys

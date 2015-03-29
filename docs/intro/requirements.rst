.. _intro-requirements:

===================
System requirements
===================

Scrapple is a Python package/command line tool which runs on all operating systems that support `Python`_. This includes :

- Windows XP
- Windows Vista
- Windows 7
- Windows 8.x
- Common Linux distros : Ubuntu/Xubuntu/Lubuntu, Fedora, Mint, Gentoo, openSUSE, Arch Linux etc.
- OS X 

The basic requirements for running Scrapple are:

* `Python`_ 2.7 or 3.x
* *pip* or *easy_install* for installing the necessary Python packages [*pip* is the recommended choice]

.. _Python: https://www.python.org/

Scrapple depends on a number of Python packages for various parts of its execution :

- `requests`_ : The HTTP library. The requests library is used to make HTTP requests to load the required web pages.
- `lxml`_ : The web scraping library. The lxml library is used to parse the :ref:`element tree <concepts-structure>` and extract the required content. 
- `cssselect`_ : The CSS selector library. cssselect works in tandem with lxml to handle CSS Selector expressions. 
- `docopt`_ : The command line parser. The docopt library is used to parse the command line interface input based on the CLI usage specification in the docstring.
- `Jinja2`_ : The templating engine. Jinja2 is used to create skeleton :ref:`configuration file <framework-config>` and generated Python scraper scripts. 
- `Flask`_ : The web micro-framework. The web interface to edit configuration files runs on Flask.
- `colorama`_ : The output formatter. colorama is used to format the various sections of the command line output.

.. _requests: https://pypi.python.org/pypi/requests
.. _lxml: https://pypi.python.org/pypi/lxml/3.4.0
.. _cssselect: https://pypi.python.org/pypi/cssselect
.. _docopt: https://pypi.python.org/pypi/docopt
.. _Jinja2: http://jinja.pocoo.org/
.. _Flask: http://flask.pocoo.org/
.. _colorama: https://pypi.python.org/pypi/colorama

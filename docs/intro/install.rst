.. _intro-install:

================
Install Scrapple
================

The basic requirements for running Scrapple are:

* `Python2.7`_ 
* *pip* or *easy_install* [*pip* is the recommended choice]

.. _Python2.7: https://www.python.org/downloads/release/python-278/

If you're running Ubuntu, install the necessary C libraries for the lxml module.

``$ sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev``

If you're running any other Linux distro, follow the standard install procedures and install these libraries.

You may not have to do this on your Windows machine.

Install the requirements for running Scrapple with

``$ pip install -r requirements.txt``

If this fails because of the access privileges, run the command with ``sudo``.

You can then install Scrapple with 

``$ pip install scrapple`` or ``$ sudo pip install scrapple``

To verify that Scrapple has been installed correctly, try the ``scrapple`` command from the command line.

``$ scrapple --version``

This should display the version of Scrapple installed.

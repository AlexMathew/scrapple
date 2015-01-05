================
Install Scrapple
================

The basic requirements for running Scrapple are:

* `Python2.7`_ 
* *pip* or *easy_install* [*pip* is the recommended choice]

.. _Python2.7: https://www.python.org/downloads/release/python-278/

On your Linux machine, install the necessary C libraries for the lxml module.

``$ sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev``

Install the requirements for running Scrapple with

``$ pip install -r requirements.txt``

If this fails because of the access privileges, run the command with ``sudo``.

You can then install Scrapple with 

``$ pip install Scrapple`` or ``$ sudo pip install Scrapple``

To verify that Scrapple has been installed correctly, try the ``scrapple`` command from the command line.

``$ scrapple -V``

This should display the version of Scrapple installed.

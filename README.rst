========
Scrapple
========

.. image:: https://travis-ci.org/scrappleapp/scrapple.svg
    :target: https://travis-ci.org/scrappleapp/scrapple
    :alt: Travis-CI Build Status

.. image:: https://pypip.in/download/scrapple/badge.svg
    :target: https://pypi.python.org/pypi//scrapple
    :alt: Downloads

.. image:: https://pypip.in/version/scrapple/badge.svg?text=version
    :target: https://pypi.python.org/pypi/scrapple
    :alt: Latest Version


`Scrapple`_ is a framework for creating web scrapers and web crawlers according to a key-value based configuration file. It provides a command line interface to run the script on a given JSON-based configuration input, as well as a web interface to provide the necessary input.

The primary goal of Scrapple is to abstract the process of designing web content extractors. The focus is laid on what to extract, rather than how to do it. The user-specified configuration file contains selector expressions (XPath expressions or CSS selectors) and the attribute to be selected. Scrapple does the work of running this extractor, without the user worrying about writing a program. Scrapple can also be used to generate a Python script that implements the desired extractor.

.. _Scrapple: http://scrappleapp.github.io/scrapple

Installation
============

You can install Scrapple by using

::

	$ sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev
	$ pip install scrapple

Otherwise, you could clone this repository and install the package.

::
	
	$ git clone http://github.com/scrappleapp/scrapple scrapple
	$ cd scrapple
	$ pip install -r requirements.txt
	$ python setup.py install

Tutorials
=========

(Updates soon)


Documentation
=============

You can read the `complete documentation`_ for an extensive coverage on the background behind Scrapple, a thorough explanation on the Scrapple package implementation and a complete coverage of tutorials on how to use Scrapple to run your scraper/crawler jobs.

.. _complete documentation: http://scrapple.rtfd.org

Authors
=======

Scrapple is maintained by `Alex Mathew`_ and `Harish Balakrishnan`_.

.. _Alex Mathew: http://github.com/AlexMathew
.. _Harish Balakrishnan: http://github.com/harishb93

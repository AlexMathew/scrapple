.. Scrapple documentation master file, created by
   sphinx-quickstart on Sat Nov 22 00:06:38 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
Scrapple |version| documentation
=================================

The Internet is a huge source of information. Several people may use data from the Internet to perform various activities, like research or analysis. Data extraction is a primary step involved in data mining and analysis. Extracting content from structured web pages is a vital task to be performed when the Internet is the principal source of data.

The current standards in web structure involve the use of CSS selectors or XPath expressions to select particular tags from which information can be extracted. Web pages are structured as element trees which can be parsed to traverse through the tags. This tree structure, which represents tags as parent/children/siblings, is very useful when tags should be represented in terms of the rest of the web page structure.

Scrapple is a project aimed at designing a framework for building web content extractors. Scrapple uses key-value based configuration files to define parameters to be considered in generating the extractor. It considers the base page URL, selectors for the data to be extracted, and the selector for the links to be crawled through. At its core, Scrapple abstracts the implementation of the extractor, focussing more on representing the selectors for the required tags. Scrapple can be used to generate single page content extractors or link crawlers. 

This documentation contains information about how to use Scrapple and how Scrapple works. 

Overview
========

.. toctree::
   :maxdepth: 3
   :hidden:

   intro/overview
   intro/install

:doc:`intro/overview`
    An introduction to Scrapple

:doc:`intro/install`
    Instructions for installing Scrapple and the required dependencies

.. _section-concepts:

Concepts
========

.. toctree::
   :maxdepth: 3
   :hidden:



.. _section-framework:

The Scrapple framework
======================

.. toctree::
   :maxdepth: 3
   :hidden:

   framework/commands
   framework/config

:doc:`framework/commands`
    Commands provided by the Scrapple CLI

:doc:`framework/config`
    The configuration file which is used by Scrapple to implement the required extractor/crawler

.. _section-implementation:

Implementation
==============

.. toctree::
   :maxdepth: 3
   :hidden:


.. _section-tutorials:

Tutorials
=========

.. toctree::
   :maxdepth: 3
   :hidden:

   intro/tutorial
   intro/tutorials/single_linear
   intro/tutorials/link_crawler

:doc:`intro/tutorial`
    Introduction to the Scrapple tutorials

:doc:`intro/tutorials/single_linear`
    Tutorial for single page linear extractors

:doc:`intro/tutorials/link_crawler`
    Tutorial for link crawlers

Contribution guide
==================

This part contains information about contributing to the project.

.. toctree::
   :maxdepth: 3
   :hidden:

   dev/authors
   dev/contributing

:doc:`dev/authors`
    Contributors to the project

:doc:`dev/contributing`
    Details about contributing to Scrapple
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


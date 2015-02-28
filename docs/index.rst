.. Scrapple documentation master file, created by
   sphinx-quickstart on Sat Nov 22 00:06:38 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
Scrapple |version| documentation
=================================

Scrapple is a project aimed at designing a framework for building web content extractors. Scrapple uses key-value based configuration files to define parameters to be considered in generating the extractor. It considers the base page URL, selectors for each data to be extracted, and the selector for the links to be crawled through. 

Scrapple can be used to generate single page content extractors or link crawlers. 

This documentation contains information about how to use Scrapple and how Scrapple works. 

Overview
========

.. toctree::
   :hidden:

   intro/overview
   intro/install
   intro/tutorial
   intro/tutorials/single_linear
   intro/tutorials/link_crawler

:doc:`intro/overview`
    An introduction to Scrapple

:doc:`intro/install`
    Instructions for installing Scrapple and the required dependencies

:doc:`intro/tutorial`
    An intoductory tutorial to using Scrapple for generating the required scrapers/crawlers

.. _section-basics:

Concepts
========

.. toctree::
   :hidden:

   topics/commands
   topics/config

:doc:`topics/commands`
    Commands provided by the Scrapple CLI

:doc:`topics/config`
    The configuration file which is used by Scrapple to implement the required extractor/crawler


Contribution guide
==================

This part contains information about contributing to the project.

.. toctree::
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


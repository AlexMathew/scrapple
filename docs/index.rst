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

Web content extraction is a common task in the process of collecting data for data analysis. There are several existing frameworks that aid in this task. In this chapter, a brief introduction of Scrapple is provided, with instructions on setting up the development machine to run Scrapple. 

.. toctree::
   :maxdepth: 2
   :hidden:

   intro/overview
   intro/existing
   intro/requirements
   intro/install

:doc:`intro/overview`
    An introduction to Scrapple

:doc:`intro/existing`
    A review of existing systems

:doc:`intro/requirements`
    Hardware and software requirements to run Scrapple

:doc:`intro/install`
    Instructions for installing Scrapple and the required dependencies

.. _section-concepts:

Concepts
========

Creating web content extractors requires a good understanding of the following topics :

- :doc:`concepts/structure`
- :doc:`concepts/selectors`
- :doc:`concepts/formats`

In this chapter, a brief overview of the concepts behind Scrapple is given.

.. toctree::
   :maxdepth: 2
   :hidden:

   concepts/structure
   concepts/selectors
   concepts/formats

:doc:`concepts/structure`
    The basics of web page structure and element trees

:doc:`concepts/selectors`
    An introduction to tag selector expressions

:doc:`concepts/formats`
    The primary data formats involved in handling data

.. _section-framework:

The Scrapple framework
======================

.. toctree::
   :maxdepth: 2
   :hidden:

   framework/basic
   framework/commands
   framework/config

:doc:`framework/basic`
    How Scrapple works

:doc:`framework/commands`
    Commands provided by the Scrapple CLI

:doc:`framework/config`
    The configuration file which is used by Scrapple to implement the required extractor/crawler

.. _section-implementation:

Implementation
==============

.. toctree::
   :maxdepth: 2
   :hidden:


.. _section-tutorials:

Tutorials
=========

In this section, we'll cover some basic tutorials for using Scrapple. We'll cover two basic types of tools you can build with Scrapple.

- :doc:`intro/tutorials/single_linear`
- :doc:`intro/tutorials/link_crawler`

Once you've :doc:`installed Scrapple <intro/install>`, you can see the list of available commands and the related options using the command

``$ scrapple --help``


The description for the commands provided by Scrapple are described in the :ref:`commands <framework-commands>` section.

The :ref:`configuration file <framework-config>` is the backbone of Scrapple. It specifies the base page URL, selectors for the data extraction, the follow link for the link crawler and several other parameters. 

Examples for each type are given. 


.. toctree::
   :maxdepth: 2
   :hidden:

   intro/tutorials/single_linear
   intro/tutorials/link_crawler

:doc:`intro/tutorials/single_linear`
    Tutorial for single page linear extractors

:doc:`intro/tutorials/link_crawler`
    Tutorial for link crawlers

.. _section-results:

Experimentation & Results
=========================

.. toctree::
   :maxdepth: 2
   :hidden:


.. _section-conclusion:

Conclusion & Future Work
========================

.. toctree::
   :maxdepth: 2
   :hidden:


Contribution guide
==================

This part contains information about contributing to the project.

.. toctree::
   :maxdepth: 2
   :hidden:

   dev/authors
   dev/contributing

:doc:`dev/authors`
    Contributors to the project

:doc:`dev/contributing`
    Details about contributing to Scrapple
   

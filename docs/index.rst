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


.. Introduction
.. ============

.. The Internet is a huge source of information. Several people may use data from the Internet to perform various activities, like research or analysis. However, there are two primary issues involved with using data from the Internet :

.. * You may not have any way to get information from a particular website, i.e, it may not provide an API for accessing the data.

.. * Even if an API is provided, it may not give all the data needed. It is possible that there may be some data that is present on the web interface, but not provided through the API.

.. This is where web scrapers and web crawlers come in. 

.. Web scrapers & web crawlers
.. ---------------------------

.. **Web scrapers**, also called **extractors**, are used to extract content from any particular page. They may use CSS Selectors or XPath expressions to point to a particular tag on the HTML structure of the page, and extract the content from that tag. The content extracted could be text from ``<div>`` tags, links from ``<a>`` tags, and so on.

.. **Web crawlers** are scripts that go through multiple links from a single base page. Given a base URL, it uses this page as an index page to many different pages. It goes through each of these pages, extracting the required content along the way. 

.. Scrapers and crawlers can be written to extract necessary content from any page that you would need information from. 

.. Objective
.. ---------

.. Scrapple helps to reduce the hassle in manually writing the scripts needed to extract the required content. It involves the use of a configuration file that specifies property-value pairs of various parameters involved in constructing the required script. 

.. The configuration file is a JSON document, consisting of the required key-value pairs. The user specifies the base URL of the page to work on, and also the tags of the data to be extracted. The user has a choice between CSS selectors and XPath expressions for specifying the target tags. Once the target tags have been specified, the other parameters are filled and the configuration file is completed. This configuration file is used by Scrapple to generate the required script and the execution is performed to generate the output of the scraper as a CSV/JSON document (depending on the argument passed while running the script). Thus, the user can obtain data they need without having extensive programming expertise to manually write the scripts required. 

.. Application of Scrapple
.. -----------------------

.. Scrapple can be used to create custom web content extractors, to build datasets required for various applications. 

.. For example, to perform an analysis of the `trending repositories on GitHub <http://github.com/trending/>`_, the user would require a dataset of statistics, like commits on each repository, number of followers of the repository etc. To obtain this data, the user could use Scrapple to create an extractor, that would crawl through the repository list on the page and extract the required data for each repository. 

.. Scrapple is experimented with an :ref:`example of talk listings from Pyvideo <section-experimentation>`.


.. The inspiration behind Scrapple
.. -------------------------------

.. Scrapple is based on the best ideas involved in two projects :

.. * Scrapy [1] : Scrapy is an application framework, designed to build web spiders that extract structured web data.
.. * Ducky [2] : Ducky is a semi-automatic web wrapper, which uses a configuration file to define extraction rules, and extract data accordingly.


.. Project timeline
.. ================

.. The overall project work can be summarized in this Gantt chart.

.. .. figure:: intro/images/gantt.png
..   :alt: Gantt chart
..   :align: center

..   Gantt chart - Project timeline

.. The metrics on `the Scrapple GitHub repository <http://github.com/scrappleapp/scrapple>`_ can be used to visually represent the contributions to the project over the duration of the project work.

.. .. figure:: intro/images/commits.png
..   :alt: GitHub commits
..   :align: center

..   Commit frequency on the project

.. .. figure:: intro/images/weekly.png
..   :alt: Weekly contributions
..   :align: center

..   Weekly contributions to the project repository


.. Review of existing systems
.. ==========================

.. Data extraction process from the web can be classified based on the selectors used. Selectors can be CSS or XPath expressions. CSS selectors are said to be faster and are used by many browsers. Ducky [2] uses CSS selectors for extracting data from pages that are similarly structured. 

.. On the other hand, XPath expressions are more reliable, handles text recognition better and a powerful option to locate elements when compared to CSS selectors. Many researches are going on presently in this topic. Oxpath [3] provides an extension for XPath expressions. The system created by V. Crescenzi, P. Merialdo, and D. Qiu [4] uses XPath expressions for locating the training data to create queries posed to the workers of a crowd sourcing platform. 

.. Systems like Ducky and Deixto [5] use the concept of Configuration files where the user inputs the simple details like base pages, a “next” column if there are multiple pages to be parsed. Deixto uses the concept of tag filtering where the unnecessary html tags can be ignored when the DOM (Document Object Model) tree is created.

.. Scrapy [1], an open source project, provides the framework for web crawlers and extractors. This framework provides support for spider programs that are manually written to extract data from the web. It uses XPath expression to locate the content. The output formats of Ducky and Scrapy include XML, CSV and JSON files.


.. Concepts
.. ========

.. Creating web content extractors requires a good understanding of the following topics :

.. - :doc:`concepts/structure`
.. - :doc:`concepts/selectors`
.. - :doc:`concepts/formats`

.. A brief overview of the concepts behind Scrapple is given.

.. .. toctree::
..    :maxdepth: 2
..    :hidden:

..    concepts/structure
..    concepts/selectors
..    concepts/formats


 
.. Requirement specification & Installation instructions
.. =====================================================

.. .. toctree::
..    :maxdepth: 2
..    :hidden:

..    intro/requirements
..    intro/install

.. Interaction scenarios
.. =====================

.. The primary use cases in Scrapple are the execution of the :ref:`commands <framework-commands>` provided by the framework. A general idea of the execution of these commands and the relation between the various modules of the framework can be understood through a study of the interaction scenarios for each of the commands. 

.. Basic sequence diagrams for the execution for each command can be represented as such. A more detailed explanation of the execution of the commands is provided in the :ref:`commands implementation <implementation-commands>` section.

.. .. figure:: implementation/images/genconfig.jpg
..   :alt: Genconfig sequence diagram
..   :align: center

..   :ref:`Genconfig command<command-genconfig>`

.. .. figure:: implementation/images/generate.jpg
..   :alt: Generate sequence diagram
..   :align: center

..   :ref:`Generate command<command-generate>`

.. .. figure:: implementation/images/run.jpg
..   :alt: Run sequence diagram
..   :align: center

..   :ref:`Run command<command-run>`

.. .. figure:: implementation/images/web.jpg
..   :alt: Web sequence diagram
..   :align: center

..   :ref:`Web command<command-web>`

.. Implementation methodology
.. ==========================

.. This section deals with how Scrapple works - the architecture of the Scrapple framework, the commands and options provided by the framework and the specification of the configuration file.

.. It also deals with the implementation of the Scrapple framework. This includes an explanation of the classes involved in the framework, the interaction scenarios for each of the commands supported by Scrapple, and utility functions that form a part of the implementation of the extractor. 

.. .. toctree::
..    :maxdepth: 2
..    :hidden:

..    framework/basic
..    framework/commands
..    framework/config
..    implementation/classes
..    implementation/cli
..    implementation/commands
..    implementation/selectors
..    implementation/utils

.. .. _section-experimentation:

.. Experimentation & Results
.. =========================

.. In this section, some experiments with Scrapple are provided. There are two main types of tools that can be implemented with the Scrapple framework :

.. - :doc:`intro/tutorials/single_linear`
.. - :doc:`intro/tutorials/link_crawler`

.. Once you've :doc:`installed Scrapple <intro/install>`, you can see the list of available :ref:`commands <framework-commands>` and the related options using the command

.. ``$ scrapple --help``

.. The :ref:`configuration file <framework-config>` is the backbone of Scrapple. It specifies the base page URL, selectors for the data extraction, the follow link for the link crawler and several other parameters. 

.. Examples for each type are given. 

.. .. toctree::
..    :maxdepth: 2
..    :hidden:

..    intro/tutorials/single_linear
..    intro/tutorials/link_crawler
..    intro/tutorials/results


.. Conclusion & Future Work
.. ========================

.. The goal of Scrapple is to provide a generalized solution to the problem of web content extraction. This framework requires a basic understanding of web page structure, which is necessary to write the necessary selector expressions. Using these selector expressions, the required web content extractors can be implemented to generate the desired datasets. 

.. Experimentation with a wide range of websites gave consistently accurate results, in terms of the generated dataset. However, larger crawl jobs took a lot of time to complete and it was necessary to run the execution in one stretch. Scrapple could be improved to provide restartable crawlers, using caching mechanisms to keep track of the position in the URL frontier. Tag recommendation systems could also be implemented, using complex learning algorithms, though there would be a trade-off on accuracy.

.. Improvements to the existing features would include a complete development of the web based configuration file editor, to support editing configuration files for link crawlers.



.. Appendix
.. ========

.. Plagiarism report
.. -----------------

.. .. image:: intro/images/plagiarism.jpg
..    :alt: Plagiarism report
..    :align: center


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

This section deals with how Scrapple works - the architecture of the Scrapple framework, the commands and options provided by the framework and the specification of the configuration file.


.. toctree::
   :maxdepth: 2
   :hidden:

   framework/basic
   framework/commands
   framework/config

:doc:`framework/basic`
    The architecture of the Scrapple framework

:doc:`framework/commands`
    Commands provided by the Scrapple CLI

:doc:`framework/config`
    The configuration file which is used by Scrapple to implement the required extractor/crawler

.. _section-implementation:

Implementation
==============

This section deals with the implementation of the Scrapple framework. This includes an explanation of the classes involved in the framework, the interaction scenarios for each of the commands supported by Scrapple, and utility functions that form a part of the implementation of the extractor. 

.. toctree::
   :maxdepth: 2
   :hidden:

   implementation/classes
   implementation/interaction
   implementation/cli
   implementation/commands
   implementation/selectors
   implementation/utils

:doc:`implementation/classes`
    The classes involved in the implementation of Scrapple

:doc:`implementation/interaction`
    Interaction scenarios in the implementation of each of the Scrapple commands

:doc:`implementation/cli`
    The Scrapple command line interface

:doc:`implementation/commands`
    The implementation of the command classes

:doc:`implementation/selectors`
    The implementation of the selector classes

:doc:`implementation/utils`
    Utilities functions that support the implementation of the extractor

   
.. _section-tutorials:

Experimentation & Results
=========================

In this section, some experiments with Scrapple are provided. There are two main types of tools that can be implemented with the Scrapple framework :

- :doc:`intro/tutorials/single_linear`
- :doc:`intro/tutorials/link_crawler`

Once you've :doc:`installed Scrapple <intro/install>`, you can see the list of available :ref:`commands <framework-commands>` and the related options using the command

``$ scrapple --help``

The :ref:`configuration file <framework-config>` is the backbone of Scrapple. It specifies the base page URL, selectors for the data extraction, the follow link for the link crawler and several other parameters. 

Examples for each type are given. 

.. toctree::
   :maxdepth: 2
   :hidden:

   intro/tutorials/single_linear
   intro/tutorials/link_crawler
   intro/tutorials/results

:doc:`intro/tutorials/single_linear`
    Tutorial for single page linear extractors

:doc:`intro/tutorials/link_crawler`
    Tutorial for link crawlers


Contributing to Scrapple
========================

Scrapple is on `GitHub <http://github.com/scrappleapp/scrapple>`_ !

.. toctree::
   :maxdepth: 2
   :hidden:

   contributing/authors
   contributing/history
   contributing/guide

:doc:`contributing/authors`
    The creators of Scrapple

:doc:`contributing/history`
    History of Scrapple releases

:doc:`contributing/guide`
    The Scrapple contribution guide


.. _section-conclusion:


The goal of Scrapple is to provide a generalized solution to the problem of web content extraction. This framework requires a basic understanding of web page structure, which is necessary to write the necessary selector expressions. Using these selector expressions, the required web content extractors can be implemented to generate the desired datasets. 

Experimentation with a wide range of websites gave consistently accurate results, in terms of the generated dataset. However, larger crawl jobs took a lot of time to complete and it was necessary to run the execution in one stretch. Scrapple could be improved to provide restartable crawlers, using caching mechanisms to keep track of the position in the URL frontier. Tag recommendation systems could also be implemented, using complex learning algorithms, though there would be a trade-off on accuracy.

.. toctree::
   :maxdepth: 2
   :hidden:

.. _intro-overview:

====================
Introducing Scrapple
====================

The Internet is a huge source of information. Several people may use data from the Internet to perform various activities, like research or analysis. However, there are two primary issues involved with using data from the Internet :

* You may not have any way to get information from a particular website, i.e, it may not provide an API for accessing the data.

* Even if an API is provided, it may not give all the data needed. It is possible that there may be some data that is present on the web interface, but not provided through the API.

This is where web scrapers and web crawlers come in. 

Web scrapers & web crawlers
===========================

**Web scrapers**, also called **extractors**, are used to extract content from any particular page. They may use CSS Selectors or XPath expressions to point to a particular tag on the HTML structure of the page, and extract the content from that tag. The content extracted could be text from ``<div>`` tags, links from ``<a>`` tags, and so on.

**Web crawlers** are scripts that go through multiple links from a single base page. Given a base URL, it uses this page as an index page to many different pages. It goes through each of these pages, extracting the required content along the way. 

Scrapers and crawlers can be written to extract necessary content from any page that you would need information from. 

How Scrapple helps
==================

Scrapple helps to reduce the hassle in manually writing the scripts needed to extract the required content. It involves the use of a configuration file that specifies property-value pairs of various parameters involved in constructing the required script. 

The configuration file is a JSON document, consisting of the required key-value pairs. The user specifies the base URL of the page to work on, and also the tags of the data to be extracted. The user has a choice between CSS selectors and XPath expressions for specifying the target tags. Once the target tags have been specified, the other parameters are filled and the configuration file is completed. This configuration file is used by Scrapple to generate the required script and the execution is performed to generate the output of the scraper as a CSV/JSON document (depending on the argument passed while running the script). Thus, the user can obtain data they need without having extensive programming expertise to manually write the scripts required. 

The inspiration behind Scrapple
===============================

Scrapple is based on the best ideas involved in two projects :

* `Scrapy`_ : An application framework for crawling web sites and extracting structured data.
* `Ducky`_ : A semi-automatic Web Wrapper to extract data according to the pre-defined and simple data extraction rule in the configuration file.


.. _Scrapy: http://scrapy.org
.. _Ducky: http://dl.acm.org/citation.cfm?id=2628244

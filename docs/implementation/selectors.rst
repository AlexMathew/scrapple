.. _implementation-selectors:

Selector classes
================

:ref:`Selectors <concepts-selectors>` are used to specifically point to certain tags on a web page, from which content has to be extracted. In Scrapple, selectors are implemented through selector classes, which define methods to extract necessary content through specified selector expressions and to extract links from anchor tags to be crawled through. 

There are two selector types that are supported in Scrapple : 

* XPath expressions
* CSS selector expressions

These selector types are implemented through the ``XpathSelector`` and ``CssSelector`` classes, respectively. These two classes use the ``Selector`` class as their super class. 

In the super class, the URL of the web page to be loaded is validated - ensuring the schema has been specified, and that the URL is valid. A HTTP GET request is made to load the web page, and the HTML content of this fetched web page is used to generate the :ref:`element tree <concepts-structure>`. This is the element tree that will be parsed to extract the necessary content.


.. automodule:: scrapple.selectors.xpath

.. autoclass:: scrapple.selectors.xpath.XpathSelector
   :members:

.. automodule:: scrapple.selectors.css

.. autoclass:: scrapple.selectors.css.CssSelector
   :members:

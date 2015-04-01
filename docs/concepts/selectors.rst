.. _concepts-selectors:

====================
Selector expressions
====================

Selector expressions are used to point to specific groups of tags on a web page. They involve using the tag type and tag attributes to select certain sections of the page.

There are two main types of selector expressions that are commonly used, and supported by Scrapple :

* CSS selectors
* XPath expressions

CSS Selectors
=============

CSS selectors [7] offer flexible options to design efficient and dynamic tag queries, providing variety of expression and simplicity. They use tag names and tag attributes to represent the traversal through the DOM tree. 

For example, 

``div#sidebar dl dd a`` refers to an anchor tag that is under a definition list in the ``<div>`` with a id 'sidebar'.

In recent times, the use of CSS selectors is becoming more common because of the development of Javascript libraries (like jQuery and React.js) which use CSS selectors to access particular tags in the web page structure.

CSS selectors are faster in many browsers. They rely on the structure as well as the attributes of the page to find elements. They provide a good balance between structure and attributes. Though the property values cannot be specified as expressions, it is widely used due to its simplicity and flexibility. They can traverse down a DOM(Document Object Model) according to the path specified in the selector expression. 

`A detailed study on CSS selectors can be found on W3C <http://www.w3.org/TR/CSS21/selector.html>`_.

XPath Selectors
===============

XPath [8] is used for navigating documents and selecting nodes. It is based on a tree representation [9] of the document it is to be traversed. Since it can traverse both up and down the DOM, it is used widely used for easy navigation through the page to locate the elements searched for. 
Here are few simple examples of XPath expressions and their meaning.

* ``/html/body/p[1]`` : This finds the first p inside the body section of the html
* ``//link`` : This selects all the link tags in the page
* ``//div[@id="commands"]`` : This selects the div elements which contain the id="commands"

XPath expressions can be simplified by looking up for path having unique attributes in the page. For instance, consider the expression 

::

	//*[@id="guide-container"]/div/ul/li[1]/ \
	div/ul/li[@id="what_to_watch-guide-item"]/a

This can be simplified further as ``//*[@id="what_to_watch-guide-item"]/a`` based on the unique id=”what_to_watch-guide-item” attribute used. 

They can also be simplified by shortening the reference path. For instance, consider the same expression as the previous example. This expression can be shortened as ``//*[@id="guide-container"]//li[@id="what_to_watch-guide-item"]/a`` where the '//' refers to the shortened path.

There are several other advanced methods of representing XPath expressions, like expressing the ancestors or siblings, normalizing spaces etc.

`A detailed study on XPath expressions can be found on W3C <http://www.w3.org/TR/xpath/>`_.

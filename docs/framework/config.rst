.. _framework-config:

==================
Configuration file
==================

The configuration file is the basic specification of the extractor required. It contains the URL for the web page to be loaded, the selector expressions for the data to be extracted and in the case of crawlers, the selector expression for the links to be crawled through. 

The keys used in the configuration file are :

- **project_name** : Specifies the name of the project with which the configuration file is associated.
- **selector_type** : Specifies the type of selector expressions used. This could be "xpath" or "css".
- **scraping** : Specifies parameters for the extractor to be created.
	* **url** : Specifies the URL of the base web page to be loaded.
	* **data** : Specifies a list of selectors for the data to be extracted.
		+ **selector** : Specifies the selector expression.
		+ **attr** : Specifies the attribute to be extracted from the result of the selector expression.
		+ **field** : Specifies the field name under which this data is to stored.
		+ **default** : Specifies the default value to be used if the selector expression fails.
	* **next** : Specifies the crawler implementation.
		+ **follow_link** : Specifies the selector expression for the ``<a>`` tags to be crawled through.

The main objective of the configuration file is to specify extraction rules in terms of selector expressions and the attribute to be extracted. There are certain set forms of selector/attribute value pairs that perform various types of content extraction.

Selector expressions :

- CSS selector or XPath expressions that specify the tag to be selected.
- "url" to take the URL of the current page on which extraction is being performed. 

Attribute selectors :

- "text" to extract the textual content from that tag.
- "href", "src" etc., to extract any of the other attributes of the selected tag.

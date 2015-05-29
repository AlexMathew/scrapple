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

How to use Scrapple
===================

Scrapple provides 4 commands to create and implement extractors.

- `genconfig`_
- `generate`_
- `run`_
- `web`_

.. _genconfig: http://scrapple.readthedocs.org/en/latest/framework/commands.html#genconfig
.. _generate: http://scrapple.readthedocs.org/en/latest/framework/commands.html#generate
.. _run: http://scrapple.readthedocs.org/en/latest/framework/commands.html#run
.. _web: http://scrapple.readthedocs.org/en/latest/framework/commands.html#web

Scrapple implements the desired extractor on the basis of the user-specified configuration file. There are guidelines regarding how to write these configuration files.

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


Tutorials
=========

[For a more detailed tutorial, check out the `tutorial in the documentation`_]

.. _tutorial in the documentation: http://scrapple.readthedocs.org/en/latest/#experimentation-results

In this simple example for using Scrapple, we'll extract NBA player information from `the ESPN website <http://espn.go.com/nba/teams>`_.

To first create the skeleton configuration file, we use the genconfig command.

::

	$ scrapple genconfig nba http://espn.go.com/nba/teams --type=crawler --levels=2


This creates nba.json - a sample Scrapple configuration file for a crawler, which uses XPath expressions as selectors. This can be edited and the required follow link selector, data selectors and attributes can be specified.

.. code-block:: javascript

	{
		"project_name": "nba",
		"selector_type": "xpath",
		"scraping": {
			"url": "http://espn.go.com/nba/teams",
			"data": [
				{
					"field": "",
					"selector": "",
					"attr": "",
					"default": ""
				}
			],
			"next": [
				{
					"follow_link": "//*[@class='mod-content']//a[3]",
					"scraping": {
						"data": [
							{
								"field": "team",
								"selector": "//h2",
								"attr": "text",
								"default": "<no_team>"
							}
						],
						"next": [
							{
								"follow_link": "//*[@class='mod-content']/table[1]//tr[@class!='colhead']//a",
								"scraping": {
									"data": [
										{
											"field": "name",
											"selector": "//h1",
											"attr": "text",
											"default": "<no_name>"
										},
										{
											"field": "headshot_link",
											"selector": "//*[@class='main-headshot']/img",
											"attr": "src",
											"default": "<no_image>"
										},
										{
											"field": "number & position",
											"selector": "//ul[@class='general-info']/li[1]",
											"attr": "text",
											"default": "<00> #<GFC>"
										},
										{
											"field": "stat1 career",
											"selector": "//table[@class='header-stats']//tr[@class='career']/td[1]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "stat2 career",
											"selector": "//table[@class='header-stats']//tr[@class='career']/td[2]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "stat3 career",
											"selector": "//table[@class='header-stats']//tr[@class='career']/td[3]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "stat1 season",
											"selector": "//table[@class='header-stats']//tr[1]/td[1]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "stat2 season",
											"selector": "//table[@class='header-stats']//tr[1]/td[2]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "stat3 season",
											"selector": "//table[@class='header-stats']//tr[1]/td[2]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "season PER",
											"selector": "//table[@class='header-stats']//tr[1]/td[4]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "stat1",
											"selector": "//table[@class='header-stats']//th[1]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "stat2",
											"selector": "//table[@class='header-stats']//th[2]",
											"attr": "text",
											"default": "0.0"
										},
										{
											"field": "stat3",
											"selector": "//table[@class='header-stats']//th[3]",
											"attr": "text",
											"default": "0.0"
										}												
									]
								}
							}
						]					
					}
				}
			]
		}
	}


The extractor can be run using the run command - 

::

	$ scrapple run nba nba_players -o json

This creates nba_players.json which contains the extracted data. An example snippet of this data :

.. code-block:: javascript

	{

	    "project": "nba",
	    "data": [

	        # nba_players.json continues
	        
        {
            "stat3 season": "15.0",
            "stat2 career": "9.0",
            "stat1 career": "8.0",
            "stat3": "BLKPG",
            "name": "DeAndre Jordan",
            "stat1": "PPG",
            "stat3 career": "1.7",
            "team": "Los Angeles Clippers",
            "headshot_link": "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/3442.png&w=350&h=254",
            "stat2 season": "15.0",
            "stat1 season": "11.5",
            "number & position": "#6 C",
            "season PER": "21.05",
            "stat2": "RPG"
        },
        {
            "stat3 season": "10.2",
            "stat2 career": "9.9",
            "stat1 career": "18.7",
            "stat3": "RPG",
            "name": "Chris Paul",
            "stat1": "PPG",
            "stat3 career": "4.4",
            "team": "Los Angeles Clippers",
            "headshot_link": "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/2779.png&w=350&h=254",
            "stat2 season": "10.2",
            "stat1 season": "19.1",
            "number & position": "#3 PG",
            "season PER": "26.04",
            "stat2": "APG"
        },
        {
            "stat3 season": "1.8",
            "stat2 career": "2.0",
            "stat1 career": "10.8",
            "stat3": "RPG",
            "name": "J.J. Redick",
            "stat1": "PPG",
            "stat3 career": "1.9",
            "team": "Los Angeles Clippers",
            "headshot_link": "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/3024.png&w=350&h=254",
            "stat2 season": "1.8",
            "stat1 season": "16.4",
            "number & position": "#4 SG",
            "season PER": "16.23",
            "stat2": "APG"
        },

	        # nba_players.json continues
	    ]

	}

The run command can also be used to create a CSV file with the extracted data, using the --output_type=csv argument.

The generate command can be used to generate a Python script that implements this extractor. In essence, it replicates the execution of the run command.

::

	$ scrapple generate nba nba_script -o json

This creates nba_script.py, which extracts the required data and stores the data in a JSON document.


Documentation
=============

You can read the `complete documentation`_ for an extensive coverage on the background behind Scrapple, a thorough explanation on the Scrapple package implementation and a complete coverage of tutorials on how to use Scrapple to run your scraper/crawler jobs.

.. _complete documentation: http://scrapple.rtfd.org

Authors
=======

Scrapple is maintained by `Alex Mathew`_ and `Harish Balakrishnan`_.

.. _Alex Mathew: http://github.com/AlexMathew
.. _Harish Balakrishnan: http://github.com/harishb93

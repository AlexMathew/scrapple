Scrapple
========

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7d0291fc14fe408fb865a0df195ab3e9)](https://app.codacy.com/app/AlexMathew/scrapple?utm_source=github.com&utm_medium=referral&utm_content=AlexMathew/scrapple&utm_campaign=Badge_Grade_Settings)
[![Join the chat at https://gitter.im/AlexMathew/scrapple](https://badges.gitter.im/AlexMathew/scrapple.svg)](https://gitter.im/AlexMathew/scrapple?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Scrapple on PyPI](https://badge.fury.io/py/scrapple.svg)](https://badge.fury.io/py/scrapple)
[![Build Status](https://travis-ci.org/AlexMathew/scrapple.svg?branch=master)](https://travis-ci.org/AlexMathew/scrapple)
[![Code Climate](https://codeclimate.com/github/AlexMathew/scrapple/badges/gpa.svg)](https://codeclimate.com/github/AlexMathew/scrapple)


[Scrapple](http://scrappleapp.github.io/scrapple) is a framework for creating web scrapers and web crawlers according to a key-value based configuration file. It provides a command line interface to run the script on a given JSON-based configuration input, as well as a web interface to provide the necessary input.

The primary goal of Scrapple is to abstract the process of designing web content extractors. The focus is laid on what to extract, rather than how to do it. The user-specified configuration file contains selector expressions (XPath expressions or CSS selectors) and the attribute to be selected. Scrapple does the work of running this extractor, without the user worrying about writing a program. Scrapple can also be used to generate a Python script that implements the desired extractor.

Installation
------------

You can install Scrapple by using

    $ sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev
    $ pip install scrapple

Otherwise, you could clone this repository and install the package.

    $ git clone http://github.com/scrappleapp/scrapple scrapple
    $ cd scrapple
    $ pip install -r requirements.txt
    $ python setup.py install

How to use Scrapple
-------------------

Scrapple provides 4 commands to create and implement extractors.

-   [genconfig](http://scrapple.readthedocs.org/en/latest/framework/commands.html#genconfig)
-   [generate](http://scrapple.readthedocs.org/en/latest/framework/commands.html#generate)
-   [run](http://scrapple.readthedocs.org/en/latest/framework/commands.html#run)
-   [web](http://scrapple.readthedocs.org/en/latest/framework/commands.html#web)

Scrapple implements the desired extractor on the basis of the user-specified configuration file. There are guidelines regarding how to write these configuration files.

The configuration file is the basic specification of the extractor required. It contains the URL for the web page to be loaded, the selector expressions for the data to be extracted and in the case of crawlers, the selector expression for the links to be crawled through.

The keys used in the configuration file are :

-   **project\_name** : Specifies the name of the project with which the configuration file is associated.
-   **selector\_type** : Specifies the type of selector expressions used. This could be "xpath" or "css".
-   **scraping** : Specifies parameters for the extractor to be created.  
    -   **url** : Specifies the URL of the base web page to be loaded.

    -   **data** : Specifies a list of selectors for the data to be extracted.  
        -   **selector** : Specifies the selector expression.
        -   **attr** : Specifies the attribute to be extracted from the result of the selector expression.
        -   **field** : Specifies the field name under which this data is to stored.
        -   **connector** : Specifies a text connector to join text from multiple tags (for eg, `<li>` tags)
        -   **default** : Specifies the default value to be used if the selector expression fails.

    -   **table** : Specifies a description for scraping tabular data.
        -   **table_type** : Specifies the type of table ("rows" or "columns"). This determines the type of table to be extracted. A row extraction is when there is a single row to be extracted and mapped to a set of headers. A column extraction is when a set of rows have to be extracted, giving a list of header-value mappings.
        -   **header** : Specifies the headers to be used for the table. This can be a list of headers, or a selector that gives the list of headers.
        -   **prefix** : Specifies a prefix to be added to each header.
        -   **suffix** : Specifies a suffix to be added to each header.
        -   **selector** : Specifies the selector for the data. For row extraction, this is a selector that gives the row to be extracted. For column extraction, this is a list of selectors for each column.
        -   **attr** : Specifies the attribute to be extracted from the selected tag.
        -   **connector** : Specifies a text connector to join text from multiple tags (for eg, `<li>` tags)
        -   **default** : Specifies the default value to be used if the selector does not return any data.

    -   **next** : Specifies the crawler implementation.  
        -   **follow\_link** : Specifies the selector expression for the `<a>` tags to be crawled through.

The main objective of the configuration file is to specify extraction rules in terms of selector expressions and the attribute to be extracted. There are certain set forms of selector/attribute value pairs that perform various types of content extraction.

Selector expressions :

-   CSS selector or XPath expressions that specify the tag to be selected.
-   "url" to take the URL of the current page on which extraction is being performed.

Attribute selectors :

-   "text" to extract the textual content from that tag.
-   "href", "src" etc., to extract any of the other attributes of the selected tag.

Tutorials
---------

[For a more detailed tutorial, check out the [tutorial in the documentation](http://scrapple.readthedocs.org/en/latest/#experimentation-results)]

In this simple example for using Scrapple, we'll extract NBA player information from [the ESPN website](http://espn.go.com/nba/teams).

To first create the skeleton configuration file, we use the genconfig command.

    $ scrapple genconfig nba http://espn.go.com/nba/teams --type=crawler --levels=2

This creates nba.json - a sample Scrapple configuration file for a crawler, which uses XPath expressions as selectors. This can be edited and the required follow link selector, data selectors and attributes can be specified.

~~~~ {.sourceCode .javascript}
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
                "default": "",
                "connector": ""
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
                            "default": "<no_team>",
                            "connector": ""
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
                                        "default": "<no_name>",
                                        "connector": ""
                                    },
                                    {
                                        "field": "headshot_link",
                                        "selector": "//*[@class='main-headshot']/img",
                                        "attr": "src",
                                        "default": "<no_image>",
                                        "connector": ""
                                    },
                                    {
                                        "field": "number & position",
                                        "selector": "//ul[@class='general-info']/li[1]",
                                        "attr": "text",
                                        "default": "<00> #<GFC>",
                                        "connector": ""
                                    }                                               
                                ],
                                "table": [
                                    {
                                        "table_type": "rows",
                                        "header": "//div[@class='player-stats']//table//th",
                                        "prefix": "season_",
                                        "suffix": "",
                                        "selector": "//div[@class='player-stats']//table//tr[1]/td",
                                        "attr": "text",
                                        "default": "",
                                        "connector": ""
                                    },
                                    {
                                        "table_type": "rows",
                                        "header": "//div[@class='player-stats']//table//th",
                                        "prefix": "career_",
                                        "suffix": "",
                                        "selector": "//div[@class='player-stats']//table//tr[@class='career']/td",
                                        "attr": "text",
                                        "default": "",
                                        "connector": ""
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
~~~~

The extractor can be run using the run command -

    $ scrapple run nba nba_players -o json

This creates nba\_players.json which contains the extracted data. An example snippet of this data :

~~~~ {.sourceCode .javascript}
{

    "project": "nba",
    "data": [

        # nba_players.json continues

        { 
            "career_APG" : "9.9",
            "career_PER" : "",
            "career_PPG" : "18.6",
            "career_RPG" : "4.4",
            "headshot_link" : "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/2779.png&w=350&h=254",
            "name" : "Chris Paul",
            "number & position" : "#3 PG",
            "season_APG" : "9.2",
            "season_PER" : "23.49",
            "season_PPG" : "17.6",
            "season_RPG" : "3.5",
            "team" : "Los Angeles Clippers"
        },
        { 
            "career_APG" : "3.6",
            "career_PER" : "",
            "career_PPG" : "20.3",
            "career_RPG" : "5.8",
            "headshot_link" : "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/662.png&w=350&h=254",
            "name" : "Paul Pierce",
            "number & position" : "#34 SF",
            "season_APG" : "0.9",
            "season_PER" : "7.55",
            "season_PPG" : "5.0",
            "season_RPG" : "2.6",
            "team" : "Los Angeles Clippers"
        },
        { 
            "career_APG" : "2.9",
            "career_PER" : "",
            "career_PPG" : "3.7",
            "career_RPG" : "1.8",
            "headshot_link" : "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/4182.png&w=350&h=254",
            "name" : "Pablo Prigioni",
            "number & position" : "#9 PG",
            "season_APG" : "1.9",
            "season_PER" : "8.72",
            "season_PPG" : "2.3",
            "season_RPG" : "1.5",
            "team" : "Los Angeles Clippers"
        },
        { 
            "career_APG" : "2.0",
            "career_PER" : "",
            "career_PPG" : "11.1",
            "career_RPG" : "1.9",
            "headshot_link" : "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/3024.png&w=350&h=254",
            "name" : "J.J. Redick",
            "number & position" : "#4 SG",
            "season_APG" : "1.6",
            "season_PER" : "18.10",
            "season_PPG" : "15.9",
            "season_RPG" : "1.5",
            "team" : "Los Angeles Clippers"
        },

        # nba_players.json continues
    ]

}
~~~~

The run command can also be used to create a CSV file with the extracted data, using the --output\_type=csv argument.

The generate command can be used to generate a Python script that implements this extractor. In essence, it replicates the execution of the run command.

    $ scrapple generate nba nba_script -o json

This creates nba\_script.py, which extracts the required data and stores the data in a JSON document.

Documentation
-------------

You can read the [complete documentation](http://scrapple.rtfd.org) for an extensive coverage on the background behind Scrapple, a thorough explanation on the Scrapple package implementation and a complete coverage of tutorials on how to use Scrapple to run your scraper/crawler jobs.

Authors
-------

Scrapple is maintained by [Alex Mathew](http://github.com/AlexMathew) and [Harish Balakrishnan](http://github.com/harishb93).

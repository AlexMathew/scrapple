.. _intro-tutorials-link-crawler:

=============
Link crawlers
=============

For this example, we will extract content from all talks on `pyvideo`_. We will use the `event listing`_ as the base page.

.. _pyvideo: http://pyvideo.org/
.. _event listing: http://pyvideo.org/category

To generate a skeleton configuration file, use the ``genconfig`` command. The primary arguments for the command are the project name and the URL of the base page. To generate a skeleton configuration file for a crawler, use the ``--type=crawler`` argument.

``$ scrapple genconfig pyvideo http://pyvideo.org/category --type=crawler``

This will create pyvideo.json which will initially look like this -

::

	{

	    "scraping": {
	        "url": "http://pyvideo.org/category",
	        "data": [
	            {
	                "default": "",
	                "field": "",
	                "attr": "",
	                "selector": ""
	            }
	        ],
	        "next": [
	            {
	                "follow_link": "",
	                "scraping": {
	                    "data": [
	                        {
	                            "default": "",
	                            "field": "",
	                            "attr": "",
	                            "selector": ""
	                        }
	                    ]
	                }
	            }
	        ]
	    },
	    "project_name": "pyvideo",
	    "selector_type": "xpath"

	}

You can edit this json file to specify selectors for the various data that you would want to extract from the given page.

For example, 

::

	{

	    "scraping": {
	        "url": "http://pyvideo.org/category/",
	        "data": [
	            {
	                "field": "",
	                "attr": "",
	                "selector": "",
	                "default": ""
	            }
	        ],
	        "next": [
	            {
	                "follow_link": "//table//td[1]//a",
	                "scraping": {
	                    "data": [
	                        {
	                            "field": "event",
	                            "attr": "text",
	                            "selector": "//h1",
	                            "default": ""
	                        },
	                        {
	                            "field": "event_url",
	                            "attr": "",
	                            "selector": "url",
	                            "default": ""
	                        }
	                    ],
	                    "next": [
	                        {
	                            "follow_link": "//div[@class='video-summary-data']/div[1]//a",
	                            "scraping": {
	                                "data": [
	                                    {
	                                        "field": "talk_title",
	                                        "attr": "text",
	                                        "selector": "//h3",
	                                        "default": "<unknown>"
	                                    },
	                                    {
	                                        "field": "speaker",
	                                        "attr": "text",
	                                        "selector": "//div[@id='sidebar']//dd[2]",
	                                        "default": "<unknown>"
	                                    },
	                                    {
	                                        "field": "talk_url",
	                                        "attr": "",
	                                        "selector": "url",
	                                        "default": ""
	                                    }
	                                ]
	                            }
	                        }
	                    ]
	                }
	            }
	        ]
	    },
	    "project_name": "pyvideo",
	    "selector_type": "xpath"

	}

Using this configuration file, you could generate a Python script using ``scrapple generate`` or directly run the scraper using ``scrapple run``.

The ``generate`` and ``run`` commands take two positional arguments - the project name and the output file name.

To generate the Python script -

``$ scrapple generate pyvideo talk_list``

This will create talk_list.py, which is the script that can be run to replicate the action of ``scrapple run``.

To run the scraper -

``$ scrapple run pyvideo talk_list``

This will create talk_list.json, which contains the extracted information.

A portion of the talk_list.json will look like this.

::

	{

	    "project": "pyvideo",
	    "data": [
	        {
	            "talk_title": "Boston Python Meetup: How to test the hard stuff",
	            "talk_url": "http://pyvideo.org/video/591/boston-python-meetup--how-to-test-the-hard-stuff",
	            "event_url": "http://pyvideo.org/category/15/bostonpy",
	            "speaker": "Stephan Richter",
	            "event": "Boston Python Meetup"
	        },
	        {
	            "talk_title": "Boston Python Meetup: Testing: Where do I start?",
	            "talk_url": "http://pyvideo.org/video/592/boston-python-meetup--testing--where-do-i-start",
	            "event_url": "http://pyvideo.org/category/15/bostonpy",
	            "speaker": "Marshall Weir",
	            "event": "Boston Python Meetup"
	        },
	        {
	            "talk_title": "November 2014 Chipy Talks",
	            "talk_url": "http://pyvideo.org/video/3359/november-2014-chipy-talks",
	            "event_url": "http://pyvideo.org/category/14/chipy",
	            "speaker": "Asma Mehjabeen Isaac Adorno",
	            "event": "ChiPy"
	        },


	        ### talk_list.json continues


	        {
	            "talk_title": "Python 2.7 & Python 3: A Sacred Love Story",
	            "talk_url": "http://pyvideo.org/video/3373/python-27-python-3-sacred-love-story",
	            "event_url": "http://pyvideo.org/category/64/twitter-university-2014",
	            "speaker": "Kenneth Reitz",
	            "event": "Twitter University 2014"
	        }
	    ]

	}	        

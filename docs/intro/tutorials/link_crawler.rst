.. _intro-tutorials-link-crawler:

=============
Link crawlers
=============

For this example, we will extract content from all talks on `pyvideo`_. We will use the `event listing`_ as the base page.

.. _pyvideo: http://pyvideo.org/
.. _event listing: http://pyvideo.org/category

To generate a skeleton configuration file, use the ``genconfig`` command. The primary arguments for the command are the project name and the URL of the base page. To generate a skeleton configuration file for a crawler, use the ``--type=crawler`` argument.

::

	$ scrapple genconfig pyvideo http://pyvideo.org/category \
	> --type=crawler

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
	                            "follow_link": " \
	                            //div[@id='video-summary-content']/div//strong/a \
	                            ",
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
	                                        "selector": " \
	                                        //div[@id='sidebar']//dd[2] \
	                                        ",
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

::

	$ scrapple generate pyvideo talk_list

This will create talk_list.py, which is the script that can be run to replicate the action of ``scrapple run``.

.. code-block:: python

	from __future__ import print_function
	import json
	import os

	from scrapple.selectors.xpath import XpathSelector


	def task_pyvideo():
		"""
		Script generated using 
		`Scrapple <http://scrappleapp.github.io/scrapple>`_
		"""
		results = dict()
		results['project'] = "pyvideo"
		results['data'] = list()
		try:
			r0 = dict()
			page0 = XpathSelector("http://pyvideo.org/category/")
			
			for page1 in page0.extract_links(
			"//table//td[1]//a"):
				r1 = r0.copy()
				r1["event"] = page1.extract_content(
				"//h1", "text", ""
				)
				r1["event_url"] = page1.extract_content(
				"url", "", ""
				)
				    
	    		
	    		for page2 in page1.extract_links(
	    		"//div[@class='video-summary-data']/div[1]//a"):
	    			r2 = r1.copy()
	    			r2["talk_title"] = page2.extract_content(
	    			"//h3", "text", "<unknown>"
	    			)
	    			r2["speaker"] = page2.extract_content(
	    			"//div[@id='sidebar']//dd[2]", "text", "<unknown>"
	    			)
	    			r2["talk_url"] = page2.extract_content(
	    			"url", "", ""
	    			)
	    			results['data'].append(r2)
		except KeyboardInterrupt:
			pass
		except Exception as e:
			print(e)
		finally:
			with open(os.path.join(os.getcwd(), 'talks.json'), 'w') as f:
				json.dump(results, f)
		

	if __name__ == '__main__':
		task_pyvideo()



To run the scraper -

::

	$ scrapple run pyvideo talk_list

This will create talk_list.json, which contains the extracted information.

A portion of the talk_list.json will look like this.

::

	{

	    "project": "pyvideo",
	    "data": [
	        {
	            "talk_title": "Boston Python Meetup: ...",
	            "talk_url": "http://pyvideo.org/video/591/...",
	            "event_url": "http://pyvideo.org/category/15/...",
	            "speaker": "Stephan Richter",
	            "event": "Boston Python Meetup"
	        },
	        {
	            "talk_title": "Boston Python Meetup: ...",
	            "talk_url": "http://pyvideo.org/video/592/...",
	            "event_url": "http://pyvideo.org/category/15/...",
	            "speaker": "Marshall Weir",
	            "event": "Boston Python Meetup"
	        },
	        {
	            "talk_title": "November 2014 ...",
	            "talk_url": "http://pyvideo.org/video/3359/...",
	            "event_url": "http://pyvideo.org/category/14/...",
	            "speaker": "Asma Mehjabeen Isaac Adorno",
	            "event": "ChiPy"
	        },


	        ### talk_list.json continues


	        {
	            "talk_title": "Python 2.7 & Python 3: ...",
	            "talk_url": "http://pyvideo.org/video/3373/...",
	            "event_url": "http://pyvideo.org/category/64/...",
	            "speaker": "Kenneth Reitz",
	            "event": "Twitter University 2014"
	        }
	    ]

	}	        

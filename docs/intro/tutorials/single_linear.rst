.. _intro-tutorials-single-linear:

===========================
Single page linear scrapers
===========================

For this example, we will extract content from a `pyvideo`_ page. Let us consider `the following page`_.

.. _pyvideo: http://pyvideo.org/
.. _the following page: http://pyvideo.org/video/1785/python-for-humans-1

To generate a skeleton configuration file, use the ``genconfig`` command. The primary arguments for the command are the project name and the URL of the base page. 

``$ scrapple genconfig pyvideo http://pyvideo.org/video/1785/python-for-humans-1``

This will create pyvideo.json which will initially look like this -

::

	{

	    "scraping": {
	        "url": "http://pyvideo.org/video/1785/python-for-humans-1",
	        "data": [
	            {
	                "field": "",
	                "attr": "",
	                "selector": "",
	                "default": ""
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
	        "url": "http://pyvideo.org/video/1785/python-for-humans-1",
	        "data": [
	            {
	                "field": "title",
	                "attr": "text",
	                "selector": "//h3",
	                "default": ""
	            },
	            {
	                "field": "speaker_name",
	                "attr": "text",
	                "selector": "//div[@id='sidebar']//dd[2]//a",
	                "default": ""
	            },
	            {
	                "field": "speaker_link",
	                "attr": "href",
	                "selector": "//div[@id='sidebar']//dd[2]//a",
	                "default": ""
	            },
	            {
	                "field": "event_name",
	                "attr": "text",
	                "selector": "//div[@id='sidebar']//dd[1]//a",
	                "default": ""
	            },
	            {
	                "field": "event_link",
	                "attr": "href",
	                "selector": "//div[@id='sidebar']//dd[1]//a",
	                "default": ""
	            }
	        ]
	    },
	    "project_name": "pyvideo",
	    "selector_type": "xpath"

	}

Using this configuration file, you could generate a Python script using ``scrapple generate`` or directly run the scraper using ``scrapple run``.

The ``generate`` and ``run`` commands take two positional arguments - the project name and the output file name.

To generate the Python script -

``$ scrapple generate pyvideo talk1``

This will create talk1.py, which is the script that can be run to replicate the action of ``scrapple run``.

To run the scraper -

``$ scrapple run pyvideo talk1``

This will create talk1.json, which contains the extracted information.

::

	{

	    "project": "test1",
	    "data": [
	        {
	            "event_name": "PyCon US 2013",
	            "event_link": "/category/33/pycon-us-2013",
	            "speaker_link": "/speaker/726/kenneth-reitz",
	            "speaker_name": "Kenneth Reitz",
	            "title": "Python for Humans"
	        }
	    ]

	}

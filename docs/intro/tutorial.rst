=================
Scrapple tutorial
=================

In this section, we'll cover some basic tutorials for using Scrapple. We'll cover three basic types of tools you can build with Scrapple.

- Single page linear scrapers
- Single page tabular scrapers
- Link crawlers

Once you've `installed Scrapple`_, you can see the list of available commands and the related options using the command

``$ scrapple --help``

.. _installed Scrapple: scrapple.readthedocs.org/en/latest/intro/install.html

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
	                "selector": ""
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
	                "selector": "//h3"
	            },
	            {
	                "field": "speaker_name",
	                "attr": "text",
	                "selector": "//div[@id='sidebar']//dd[2]//a"
	            },
	            {
	                "field": "speaker_link",
	                "attr": "href",
	                "selector": "//div[@id='sidebar']//dd[2]//a"
	            },
	            {
	                "field": "event_name",
	                "attr": "text",
	                "selector": "//div[@id='sidebar']//dd[1]//a"
	            },
	            {
	                "field": "event_link",
	                "attr": "href",
	                "selector": "//div[@id='sidebar']//dd[1]//a"
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

	    "event_name": "PyCon US 2013",
	    "event_link": "/category/33/pycon-us-2013",
	    "speaker_link": "/speaker/726/kenneth-reitz",
	    "speaker_name": "Kenneth Reitz",
	    "title": "Python for Humans"

	}


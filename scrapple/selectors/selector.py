"""
scrapple.selectors.selector
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
import requests
from lxml import etree


class Selector(object):
	"""
	This class defines the basic ``Selector`` object. 

	"""
	
	def __init__(self, url):
		"""
		The URL of the web page to be loaded is validated - ensuring the schema has \
		been specified, and that the URL is valid. A HTTP GET request is made to load \
		the web page, and the HTML content of this fetched web page is used to generate \
		the :ref:`element tree <concepts-structure>`. This is the element tree that will \
		be parsed to extract the necessary content.

		"""
		try:
			self.url = url
			self.content = requests.get(url).content
			self.tree = etree.HTML(self.content)
		except requests.exceptions.MissingSchema:
			raise Exception('URL should be of the form "http://<page_link>')
		except requests.exceptions.InvalidURL:
			raise Exception('The URL provided is invalid')
		except requests.exceptions.ConnectionError:
			raise Exception('Ensure that you are connected to the Internet and that the page exists')


	def extract_content(self, selector, attr, default):
		"""
		Method for performing the content extraction for the particular selector type. \
		A detailed description is provided in the derived classes. 

		"""
		raise NotImplementedError


	def extract_links(self, selector):
		"""
		Method for performing the link extraction for the crawler. \
		A detailed description is provided in the derived classes.

		"""
		raise NotImplementedError

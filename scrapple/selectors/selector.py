"""
scrapple.selectors.selector
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defines Scrapple selectors
"""

from __future__ import print_function
import requests
from lxml import etree


class Selector(object):
	"""
	Selector defines the basic selector object. 
	"""
	
	def __init__(self, url):
		try:
			self.content = requests.get(url).content
			self.tree = etree.HTML(self.content)
		except requests.exceptions.MissingSchema:
			raise Exception('URL should be of the form "http://<page_link>')
		except requests.exceptions.InvalidURL:
			raise Exception('The URL provided is invalid')
		except requests.exceptions.ConnectionError:
			raise Exception('Ensure that you are connected to the Internet and that the page exists')


	def extract_content(self, selector, attr):
		"""
		Method for performing the content extraction for the particular selector type.
		"""
		raise NotImplementedError


	def extract_links(self):
		"""
		Method for performing the link extraction for the crawler.
		"""
		raise NotImplementedError


	def extract_tabular(self):
		"""
		Method for performing the content extraction from tabular organized data.
		"""
		raise NotImplementedError

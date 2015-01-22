"""
scrapple.selectors.selector
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defines Scrapple selectors
"""

import requests

class Selector(object):
	"""
	Selector defines the basic selector object. 
	"""
	
	def __init__(self, url):
		self.content = requests.get(url).content


	def extract_content(self):
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

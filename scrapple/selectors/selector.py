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


	def extract(self):
		"""
		Method for performing the extraction for the particular selector type.
		"""
		raise NotImplementedError

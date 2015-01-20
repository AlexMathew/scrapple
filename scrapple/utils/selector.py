"""
scrapple.utils.selector
~~~~~~~~~~~~~~~~~~~~~~~

Defines Scrapple selectors
"""

import requests

class ScrappleSelector(object):
	"""
	ScrappleSelector objects allow using CSS selectors or XPath expressions \
	as needed by the user. 
	"""
	
	def __init__(self, url, selector):
		content = requests.get(url).content

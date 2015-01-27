"""
scrapple.selectors.css
~~~~~~~~~~~~~~~~~~~~~~

Defines the CSS selector
"""

from bs4 import BeautifulSoup as Soup

from scrapple.selectors.selector import Selector


class CssSelector(Selector):
	"""
	CssSelector defines the CSS selector
	"""
	
	def __init__(self, url):
		super(CssSelector, self).__init__(url)
		self.tree = Soup(self.content)


	def extract_content(self, selector):
		"""
		Method for performing the content extraction for the given CSS selector.
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

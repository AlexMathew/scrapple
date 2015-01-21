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
		super(CssSelector, self).__init__()
		self.tree = Soup(self.content)


	def extract(self):
		"""
		Method defining extraction using CSS selectors
		"""
		pass

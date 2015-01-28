"""
scrapple.selectors.css
~~~~~~~~~~~~~~~~~~~~~~

Defines the CSS selector
"""

from lxml import etree, cssselect

from scrapple.selectors.selector import Selector


class CssSelector(Selector):
	"""
	CssSelector defines the CSS selector
	"""
	
	def __init__(self, url):
		super(CssSelector, self).__init__(url)


	def extract_content(self, selector):
		"""
		Method for performing the content extraction for the given CSS selector.
		"""
		try:
			sel = cssselect.CSSSelector(selector)
			content = sel(self.tree)[0].text
			return content
		except IndexError:
			raise Exception("There is no content for the selector " + selector)


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

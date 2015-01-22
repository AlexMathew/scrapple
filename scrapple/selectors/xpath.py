"""
scrapple.selectors.xpath
~~~~~~~~~~~~~~~~~~~~~~~~

Defines the XPath selector
"""

from lxml import etree

from scrapple.selectors.selector import Selector


class XpathSelector(Selector):
	"""
	XpathSelector defines the XPath selector
	"""
	
	def __init__(self, url):
		super(XpathSelector, self).__init__()
		self.tree = etree.HTML(self.content)


	def extract_content(self):
		"""
		Method for performing the content extraction for the given XPath expression.
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

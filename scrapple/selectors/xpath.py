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


	def extract(self):
		"""
		Method defining extraction using XPath expressions
		"""
		pass

"""
scrapple.selectors.xpath
~~~~~~~~~~~~~~~~~~~~~~~~

Defines the XPath selector
"""

from scrapple.selectors.selector import Selector


class XpathSelector(Selector):
	"""
	XpathSelector defines the XPath selector
	"""
	
	def __init__(self, url):
		self.url = url
		super(XpathSelector, self).__init__(url)


	def extract_content(self, selector, attr):
		"""
		Method for performing the content extraction for the given XPath expression.
		"""
		try:
			if attr == "text":
				content = "".join([x.text for x in self.tree.xpath(selector)])
			else:
				content = self.tree.xpath(selector)[0].get(attr)
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

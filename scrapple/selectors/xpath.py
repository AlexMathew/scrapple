"""
scrapple.selectors.xpath
~~~~~~~~~~~~~~~~~~~~~~~~

Defines the XPath selector
"""

try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin

from scrapple.selectors.selector import Selector


class XpathSelector(Selector):
	"""
	XpathSelector defines the XPath selector
	"""
	
	def __init__(self, url):
		self.url = url
		super(XpathSelector, self).__init__(url)


	def extract_content(self, selector, attr, default):
		"""
		Method for performing the content extraction for the given XPath expression.
		"""
		try:
			if selector == "url":
				return self.url
			if attr == "text":
				tag = self.tree.xpath(selector)[0]
				content = " ".join([x.strip() for x in tag.itertext()])
				content = content.replace("\n", " ").strip()
			else:
				content = self.tree.xpath(selector)[0].get(attr)
				if attr in ["href", "src"]:
					content = urljoin(self.url, content)
			return content
		except IndexError:
			if default is not "":
				return default
			raise Exception("There is no content for the selector " + selector)


	def extract_links(self, selector):
		"""
		Method for performing the link extraction for the crawler.
		"""
		links = self.tree.xpath(selector)
		for link in links:
			next_url = urljoin(self.url, link.get('href'))
			yield XpathSelector(next_url)


	def extract_tabular(self):
		"""
		Method for performing the content extraction from tabular organized data.
		"""
		raise NotImplementedError

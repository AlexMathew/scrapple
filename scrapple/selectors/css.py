"""
scrapple.selectors.css
~~~~~~~~~~~~~~~~~~~~~~

Defines the CSS selector
"""

from lxml import cssselect
try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin

from scrapple.selectors.selector import Selector


class CssSelector(Selector):
	"""
	CssSelector defines the CSS selector
	"""
	
	def __init__(self, url):
		self.url = url
		super(CssSelector, self).__init__(url)


	def extract_content(self, selector, attr, default):
		"""
		Method for performing the content extraction for the given CSS selector.
		"""
		try:
			if selector == "url":
				return self.url
			sel = cssselect.CSSSelector(selector)
			if attr == "text":
				tag = sel(self.tree)[0]
				content = " ".join([x.strip() for x in tag.itertext()])
				content = content.replace("\n", " ").strip()				
			else:
				content = sel(self.tree)[0].get(attr)
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
		sel = cssselect.CSSSelector(selector)
		links = sel(self.tree)
		for link in links:
			next_url = urljoin(self.url, link.get('href'))
			yield CssSelector(next_url)


	def extract_tabular(self):
		"""
		Method for performing the content extraction from tabular organized data.
		"""
		raise NotImplementedError

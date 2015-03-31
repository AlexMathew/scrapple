"""
scrapple.selectors.css
~~~~~~~~~~~~~~~~~~~~~~

"""

from lxml import cssselect
try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin

from scrapple.selectors.selector import Selector


class CssSelector(Selector):
	"""
	The ``CssSelector`` object defines CSS selector expressions.

	"""
	
	def __init__(self, url):
		"""
		The ``Selector`` class acts as the super class for this class.

		"""
		super(CssSelector, self).__init__(url)


	def extract_content(self, selector, attr, default):
		"""
		Method for performing the content extraction for the given CSS selector.

		The cssselect library is used to handle CSS selector expressions. \
		XPath expressions have a higher speed of execution, so the given CSS selector \
		expression is translated into the corresponding XPath expression, by the \
		``cssselect.CSSSelector`` class. This selector can be used to extract content \
		from the element tree corresponding to the fetched web page.

		If the selector is "url", the URL of the current web page is returned.
		Otherwise, the selector expression is used to extract content. The particular \
		attribute to be extracted ("text", "href", etc.) is specified in the method \
		arguments, and this is used to extract the required content. If the content \
		extracted is a link (from an attr value of "href" or "src"), the URL is parsed \
		to convert the relative path into an absolute path.

		If the selector does not fetch any content, the default value is returned. \
		If no default value is specified, an exception is raised.

		:param selector: The CSS selector expression
		:param attr: The attribute to be extracted from the selected tag
		:param default: The default value to be used if the selector does not return any data
		:return: The extracted content

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
		Method for performing the link extraction for the crawler implementation.

		As in the extract_content method, the cssselect library is used to translate \
		the CSS selector expression into an XPath expression. 

		The selector passed as the argument is a selector to point to the anchor tags \
		that the crawler should pass through. A list of links is obtained, and the links \
		are iterated through. The relative paths are converted into absolute paths and \
		a ``CssSelector`` object is created with the URL of the next page as the argument \
		and this created object is yielded. 

		The extract_links method basically generates ``CssSelector`` objects for all of \
		the links to be crawled through.

		:param selector: The selector for the anchor tags to be crawled through
		:return: A ``CssSelector`` object for every page to be crawled through 
		
		"""
		sel = cssselect.CSSSelector(selector)
		links = sel(self.tree)
		for link in links:
			next_url = urljoin(self.url, link.get('href'))
			yield CssSelector(next_url)

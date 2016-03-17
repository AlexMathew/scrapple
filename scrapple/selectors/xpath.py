"""
scrapple.selectors.xpath
~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function

try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin

from lxml.etree import XPathError
from scrapple.selectors.selector import Selector


def make_ascii(s):
    """
    Convert text to ASCII
    """
    return "".join(i for i in s if ord(i) < 128)


class XpathSelector(Selector):
	"""
	The ``XpathSelector`` object defines XPath expressions.

	"""
	
	def __init__(self, url):
		"""
		The ``Selector`` class acts as the super class for this class.

		"""
		super(XpathSelector, self).__init__(url)


	def extract_content(self, selector, attr, default):
		"""
		Method for performing the content extraction for the given XPath expression.

		The XPath selector expression can be used to extract content \
		from the element tree corresponding to the fetched web page.

		If the selector is "url", the URL of the current web page is returned.
		Otherwise, the selector expression is used to extract content. The particular \
		attribute to be extracted ("text", "href", etc.) is specified in the method \
		arguments, and this is used to extract the required content. If the content \
		extracted is a link (from an attr value of "href" or "src"), the URL is parsed \
		to convert the relative path into an absolute path.

		If the selector does not fetch any content, the default value is returned. \
		If no default value is specified, an exception is raised.

		:param selector: The XPath expression
		:param attr: The attribute to be extracted from the selected tag
		:param default: The default value to be used if the selector does not return any data
		:return: The extracted content

		"""
		try:
			if selector == "url":
				return self.url
			if attr == "text":
				tag = self.tree.xpath(selector)[0]
				content = " ".join([make_ascii(x).strip() for x in tag.itertext()])
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
		except XPathError:
			raise Exception("Invalid XPath selector " + selector)


	def extract_links(self, selector):
		"""
		Method for performing the link extraction for the crawler.

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
		try:
			links = self.tree.xpath(selector)
			for link in links:
				next_url = urljoin(self.url, link.get('href'))
				yield XpathSelector(next_url)
		except XPathError:
			raise Exception("Invalid XPath selector " + selector)


	def extract_tabular(self, result={}, table_type="rows", header=[], prefix="", suffix="", selector="", attr="text", default="", verbosity=0):
		"""
		Method for performing the extraction of tabular data.

		:param result:
		:param table_type:
		:param header:
		:param prefix:
		:param suffix:
		:param selector:
		:param attr:
		:param default:
		:param verbosity:
		:return: A 2-tuple containing the list of all the column headers extracted and the list of \
		dictionaries which contain (header, content) pairs
		"""
		result_list = []
		if type(header) in [str, unicode]:
			try:
				header_list = self.tree.xpath(header)
				table_headers = [prefix + h.text + suffix for h in header_list]
			except XPathError:
				raise Exception("Invalid XPath selector " + header)
		else:
			table_headers = [prefix + h + suffix for h in header]
		if table_type not in ["rows", "columns"]:
			raise Exception("Specify 'rows' or 'columns' in table_type")
		if table_type == "rows":
			try:
				values = self.tree.xpath(selector)
				if len(table_headers) >= len(values):
					from itertools import izip_longest
					pairs = izip_longest(table_headers, values, fillvalue=default)
				else:
					from itertools import izip
					pairs = izip(table_headers, values)
				for head, val in pairs:
					if verbosity > 1:
						print("\nExtracting", head, "attribute", sep=' ', end='')
					if attr == "text":
						try:
							content = " ".join([make_ascii(x).strip() for x in val.itertext()])
						except Exception:
							content = default
						content = content.replace("\n", " ").strip()
					else:
						content = val.get(attr)
						if attr in ["href", "src"]:
							content = urljoin(self.url, content)
					result[head] = content
				result_list.append(result)
			except XPathError:
				raise Exception("Invalid XPath selector " + selector)
			except TypeError:
				raise Exception("Selector expression string to be provided. Got " + selector)
		else:
			try:
				if type(selector) in [str, unicode]:
					selectors = [selector]
				elif type(selector) == list:
					selectors = selector
				else:
					raise Exception("Use a list of selector expressions for the various columns")
				from itertools import izip, count
				pairs = izip(table_headers, selectors)
				columns = {}
				for head, selector in pairs:
					columns[head] = self.tree.xpath(selector)
				try:
					for i in count(start=0):
						r = result.copy()
						for head in columns.keys():
							if verbosity > 1:
								print("\nExtracting", head, "attribute", sep=' ', end='')
							col = columns[head][i]
							if attr == "text":
								try:
									content = " ".join([make_ascii(x).strip() for x in col.itertext()])
								except Exception:
									content = default
								content = content.replace("\n", " ").strip()
							else:
								content = col.get(attr)
								if attr in ["href", "src"]:
									content = urljoin(self.url, content)
							r[head] = content
						result_list.append(r)
				except IndexError:
					pass
			except XPathError:
				raise Exception("Invalid XPath selector " + selector)
			except TypeError:
				raise Exception("Selector expression string to be provided. Got " + selector)
		return table_headers, result_list

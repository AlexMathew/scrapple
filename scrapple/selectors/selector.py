"""
scrapple.selectors.selector
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function

import random

from scrapple.utils.text import make_ascii

import requests
from lxml import etree
from lxml.etree import XPathError

try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin


requests.warnings.filterwarnings('ignore')


class Selector(object):
	"""
	This class defines the basic ``Selector`` object. 

	"""
	__selector_type__ = ''
	

	def __init__(self, url):
		"""
		The URL of the web page to be loaded is validated - ensuring the schema has \
		been specified, and that the URL is valid. A HTTP GET request is made to load \
		the web page, and the HTML content of this fetched web page is used to generate \
		the :ref:`element tree <concepts-structure>`. This is the element tree that will \
		be parsed to extract the necessary content.

		"""
		try:
			headers = {
				'content-encoding': 'gzip', 
				'Accept-Encoding': 'identity, compress, gzip', 
				'Accept': '*/*'
			}
			headers['User-Agent'] = random.choice([
				'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0',
				'Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		        'Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0',
		        'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
		        'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
		        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
		        'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
		        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
		        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
		        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
		        'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
		        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
		        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
			])
			self.url = url
			self.content = requests.get(url, headers=headers).content
			self.tree = etree.HTML(self.content)
		except requests.exceptions.MissingSchema:
			raise Exception('URL should be of the form "http://<page_link>')
		except requests.exceptions.InvalidURL:
			raise Exception('The URL provided is invalid')
		except requests.exceptions.ConnectionError:
			raise Exception('Ensure that you are connected to the Internet and that the page exists')


	def get_tree_tag(self, selector='', get_one=False, *args, **kwargs):
		raise NotImplementedError


	def extract_content(self, selector='', attr='', default='', connector='', *args, **kwargs):
		"""
		Method for performing the content extraction for the particular selector type. \

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
		:param connector: String connector for list of data returned for a particular selector
		:return: The extracted content
		"""
		try:
			if selector.lower() == "url":
				return self.url
			if attr.lower() == "text":
				tag = self.get_tree_tag(selector=selector, get_one=True)
				content = connector.join([make_ascii(x).strip() for x in tag.itertext()])
				content = content.replace("\n", " ").strip()
			else:
				tag = self.get_tree_tag(selector=selector, get_one=True)
				content = tag.get(attr)
				if attr in ["href", "src"]:
					content = urljoin(self.url, content)
			return content
		except IndexError:
			if default is not "":
				return default
			raise Exception("There is no content for the %s selector - %s" % (self.__selector_type__, selector))
		except XPathError:
			raise Exception("Invalid %s selector - %s" % (self.__selector_type__, selector))


	def extract_links(self, selector='', *args, **kwargs):
		"""
		Method for performing the link extraction for the crawler. \

		The selector passed as the argument is a selector to point to the anchor tags \
		that the crawler should pass through. A list of links is obtained, and the links \
		are iterated through. The relative paths are converted into absolute paths and \
		a ``XpathSelector``/``CssSelector`` object (as is the case) is created with the URL of the next page as the argument \
		and this created object is yielded. 

		The extract_links method basically generates ``XpathSelector``/``CssSelector`` objects for all of \
		the links to be crawled through.

		:param selector: The selector for the anchor tags to be crawled through
		:return: A ``XpathSelector``/``CssSelector`` object for every page to be crawled through 
		
		"""
		try:
			links = self.get_tree_tag(selector=selector)
			for link in links:
				next_url = urljoin(self.url, link.get('href'))
				yield type(self)(next_url)
		except XPathError:
			raise Exception("Invalid %s selector - %s" % (self.__selector_type__, selector))
		except Exception:
			raise Exception("Invalid %s selector - %s" % (self.__selector_type__, selector))


	def extract_tabular(self, header='', prefix='', suffix='', table_type='', *args, **kwargs):
		"""
		Method for performing the tabular data extraction. \

		:param result: A dictionary containing the extracted data so far
		:param table_type: Can be "rows" or "columns". This determines the type of table to be extracted. \
		A row extraction is when there is a single row to be extracted and mapped to a set of headers. \
		A column extraction is when a set of rows have to be extracted, giving a list of header-value mappings.
		:param header: The headers to be used for the table. This can be a list of headers, or a selector that gives the list of headers
		:param prefix: A prefix to be added to each header
		:param suffix: A suffix to be added to each header
		:param selector: For row extraction, this is a selector that gives the row to be extracted. \
		For column extraction, this is a list of selectors for each column.
		:param attr: The attribute to be extracted from the selected tag
		:param default: The default value to be used if the selector does not return any data
		:param verbosity: The verbosity set as the argument for scrapple run
		:return: A 2-tuple containing the list of all the column headers extracted and the list of \
		dictionaries which contain (header, content) pairs
		"""
		if type(header) in [str, unicode]:
			try:
				header_list = self.get_tree_tag(header)
				table_headers = [prefix + h.text + suffix for h in header_list]
			except XPathError:
				raise Exception("Invalid %s selector for table header - %s" % (self.__selector_type__, header))
			except Exception:
				raise Exception("Invalid %s selector for table header - %s" % (self.__selector_type__, header))
		else:
			table_headers = [prefix + h + suffix for h in header]
		if len(table_headers) == 0:
			raise Exception("Invalid %s selector for table header - %s" % (self.__selector_type__, header))
		if table_type not in ["rows", "columns"]:
			raise Exception("Specify 'rows' or 'columns' in table_type")
		if table_type == "rows":
			result_list = self.extract_rows(table_headers=table_headers, *args, **kwargs)
		else:
			result_list = self.extract_columns(table_headers=table_headers, *args, **kwargs)
		return table_headers, result_list


	def extract_rows(self, result={}, selector='', table_headers=[], attr='', connector='', default='', verbosity=0, *args, **kwargs):
		"""
		Row data extraction for extract_tabular
		"""
		result_list = []

		try:
			values = self.get_tree_tag(selector)
			if len(table_headers) >= len(values):
				from itertools import izip_longest
				pairs = izip_longest(table_headers, values, fillvalue=default)
			else:
				from itertools import izip
				pairs = izip(table_headers, values)
			for head, val in pairs:
				if verbosity > 1:
					print("\nExtracting", head, "attribute", sep=' ', end='')
				if attr.lower() == "text":
					try:
						content = connector.join([make_ascii(x).strip() for x in val.itertext()])
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
			raise Exception("Invalid %s selector - %s" % (self.__selector_type__, selector))
		except TypeError:
			raise Exception("Selector expression string to be provided. Got " + selector)

		return result_list


	def extract_columns(self, result={}, selector='', table_headers=[], attr='', connector='', default='', verbosity=0, *args, **kwargs):
		"""
		Column data extraction for extract_tabular
		"""
		result_list = []

		try:
			if type(selector) in [str, unicode]:
				selectors = [selector]
			elif type(selector) == list:
				selectors = selector[:]
			else:
				raise Exception("Use a list of selector expressions for the various columns")
			from itertools import izip, count
			pairs = izip(table_headers, selectors)
			columns = {}
			for head, selector in pairs:
				columns[head] = self.get_tree_tag(selector)
			try:
				for i in count(start=0):
					r = result.copy()
					for head in columns.keys():
						if verbosity > 1:
							print("\nExtracting", head, "attribute", sep=' ', end='')
						col = columns[head][i]
						if attr == "text":
							try:
								content = connector.join([make_ascii(x).strip() for x in col.itertext()])
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
			raise Exception("Invalid %s selector - %s" % (self.__selector_type__, selector))
		except TypeError:
			raise Exception("Selector expression string to be provided. Got " + selector)

		return result_list

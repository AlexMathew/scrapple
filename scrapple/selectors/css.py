"""
scrapple.selectors.css
~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function

from lxml import cssselect

from scrapple.selectors.selector import Selector
from scrapple.utils.text import make_ascii


class CssSelector(Selector):
	"""
	The ``CssSelector`` object defines CSS selector expressions.

	"""
	
	__selector_type__ = 'CSS'

	
	def __init__(self, url):
		"""
		The ``Selector`` class acts as the super class for this class.

		"""
		super(CssSelector, self).__init__(url)


	def get_selected_tag(self, selector='', *args, **kwargs):
		sel = cssselect.CSSSelector(selector)
		tag = sel(self.tree)[0]
		return tag


	def get_links_for_crawling(self, selector='', *args, **kwargs):
		sel = cssselect.CSSSelector(selector)
		links = sel(self.tree)
		return links


	def extract_rows(self, *args, **kwargs):
		"""
		Row data extraction for extract_tabular
		"""
		result_list = []
		result = kwargs.get('result', {})

		try:
			sel = cssselect.CSSSelector(kwargs.get('selector', ''))
			values = sel(self.tree)
			if len(kwargs.get('table_headers', [])) >= len(values):
				from itertools import izip_longest
				pairs = izip_longest(kwargs.get('table_headers', []), values, fillvalue=kwargs.get('default', ''))
			else:
				from itertools import izip
				pairs = izip(kwargs.get('table_headers', []), values)
			for head, val in pairs:
				if kwargs.get('verbosity', 0) > 1:
					print("\nExtracting", head, "attribute", sep=' ', end='')
				if kwargs.get('attr', 'text') == "text":
					try:
						content = kwargs.get('connector', '').join([make_ascii(x).strip() for x in val.itertext()])
					except Exception:
						content = kwargs.get('default', '')
					content = content.replace("\n", " ").strip()
				else:
					content = val.get(kwargs.get('attr', 'text'))
					if kwargs.get('attr', 'text') in ["href", "src"]:
						content = urljoin(self.url, content)
				result[head] = content
			result_list.append(result)
		except TypeError:
			raise Exception("Selector expression string to be provided. Got " + kwargs.get('selector', ''))

		return result_list


	def extract_columns(self, *args, **kwargs):
		"""
		Column data extraction for extract_tabular
		"""
		result_list = []
		result = kwargs.get('result', {})

		try:
			if type(kwargs.get('selector', '')) in [str, unicode]:
				selectors = [kwargs.get('selector', '')]
			elif type(kwargs.get('selector', '')) == list:
				selectors = kwargs.get('selector', '')
			else:
				raise Exception("Use a list of selector expressions for the various columns")
			from itertools import izip, count
			pairs = izip(kwargs.get('table_headers', []), selectors)
			columns = {}
			for head, selector in pairs:
				sel = cssselect.CSSSelector(selector)
				columns[head] = sel(self.tree)
			try:
				for i in count(start=0):
					r = result.copy()
					for head in columns.keys():
						if kwargs.get('verbosity', 0) > 1:
							print("\nExtracting", head, "attribute", sep=' ', end='')
						col = columns[head][i]
						if kwargs.get('attr', 'text') == "text":
							try:
								content = kwargs.get('connector', '').join([make_ascii(x).strip() for x in col.itertext()])
							except Exception:
								content = kwargs.get('default', '')
							content = content.replace("\n", " ").strip()
						else:
							content = col.get(kwargs.get('attr', 'text'))
							if kwargs.get('attr', 'text') in ["href", "src"]:
								content = urljoin(self.url, content)
						r[head] = content
					result_list.append(r)
			except IndexError:
				pass
		except TypeError:
			raise Exception("Selector expression string to be provided. Got " + selector)

		return result_list


	def extract_tabular(self, *args, **kwargs):
		"""
		Method for performing the extraction of tabular data.

		As in the extract_content method, the cssselect library is used to translate \
		the CSS selector expression into an XPath expression. 

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
		result = kwargs.get('result', {})
		result_list = []
		if type(kwargs.get('header', [])) in [str, unicode]:
			try:
				sel = cssselect.CSSSelector(kwargs.get('header', []))
				header_list = sel(self.tree)
				table_headers = [kwargs.get('prefix', '') + h.text + kwargs.get('suffix', '') for h in header_list]
				if len(table_headers) == 0:
					raise Exception("Invalid CSS selector " + kwargs.get('header', []))
			except TypeError:
				raise Exception("Selector expression string to be provided. Got " + kwargs.get('header', []))
		else:
			table_headers = [kwargs.get('prefix', '') + h + kwargs.get('suffix', '') for h in kwargs.get('header', [])]
		if kwargs.get('table_type', 'rows') not in ["rows", "columns"]:
			raise Exception("Specify 'rows' or 'columns' in table_type")
		kwargs.update({'table_headers': table_headers})
		if kwargs.get('table_type', 'rows') == "rows":
			result_list = self.extract_rows(**kwargs)
		else:
			result_list = self.extract_columns(**kwargs)
		return table_headers, result_list

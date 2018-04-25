"""
scrapple.selectors.xpath
~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function

from scrapple.selectors.selector import Selector
from scrapple.utils.text import make_ascii


class XpathSelector(Selector):
	"""
	The ``XpathSelector`` object defines XPath expressions.

	"""
	
	__selector_type__ = 'XPath'


	def __init__(self, url):
		"""
		The ``Selector`` class acts as the super class for this class.

		"""
		super(XpathSelector, self).__init__(url)


	def get_tree_tag(self, selector='', get_one=False, *args, **kwargs):
		tags = self.tree.xpath(selector)
		if get_one:
			return tags[0]
		return tags

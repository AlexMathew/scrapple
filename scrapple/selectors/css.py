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


	def get_tree_tag(self, selector='', get_one=False, *args, **kwargs):
		sel = cssselect.CSSSelector(selector)
		tags = sel(self.tree)
		if get_one:
			return tags[0]
		return tags

"""
scrapple.utils.exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~

Functions related to handling exceptions in the input arguments
"""

import re


def handle_exceptions(args):
	"""
	Validates the arguments passed through the CLI commands.

	:param args: The arguments passed in the CLI, parsed by the docopt module
	:return: None

	"""
	projectname_re = re.compile(r'[^a-zA-Z0-9_]')
	if args['genconfig']:
		if args['--type'] not in ['scraper', 'crawler']:
			raise Exception("--type has to be 'scraper' or 'crawler'")
		if args['--selector'] not in ['xpath', 'css']:
			raise Exception("--selector has to be 'xpath' or 'css'")
	if args['generate'] or args['run']:
		if args['--output_type'] not in ['json', 'csv']:
			raise Exception("--output_type has to be 'json' or 'csv'")
	if args['genconfig'] or args['generate'] or args['run']:
		if projectname_re.search(args['<projectname>']) is not None:
			raise Exception("<projectname> should consist of letters, digits or _")
	if int(args['--levels']) < 1:
		raise Exception("--levels should be greater than, or equal to 1")
	return

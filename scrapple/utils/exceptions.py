"""
scrapple.utils.exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~

Functions related to handling exceptions in the input arguments
"""

import re

class InvalidType(ValueError):
	"""Exception class for invalid type in arguments."""
	pass


class InvalidSelector(ValueError):
	"""Exception class for invalid in arguments."""
	pass


class InvalidOutputType(ValueError):
	"""Exception class for invalid output_type in arguments."""
	pass


class InvalidProjectName(ValueError):
	"""Exception class for invalid <projectname> in arguments."""
	pass


class InvalidLevels(ValueError):
	"""Exception class for invalid levels in arguments."""
	pass


def check_arguments(args):
	"""
	Validates the arguments passed through the CLI commands.

	:param args: The arguments passed in the CLI, parsed by the docopt module
	:return: None

	"""
	projectname_re = re.compile(r'[^a-zA-Z0-9_]')
	if args['genconfig']:
		if args['--type'] not in ['scraper', 'crawler']:
			raise InvalidType("--type has to be 'scraper' or 'crawler'")
		if args['--selector'] not in ['xpath', 'css']:
			raise InvalidSelector("--selector has to be 'xpath' or 'css'")
	if args['generate'] or args['run']:
		if args['--output_type'] not in ['json', 'csv']:
			raise InvalidOutputType("--output_type has to be 'json' or 'csv'")
	if args['genconfig'] or args['generate'] or args['run']:
		if projectname_re.search(args['<projectname>']) is not None:
			message = "<projectname> should consist of letters, digits or _"
			raise InvalidProjectName(message)
	try:
		if int(args['--levels']) < 1:
			message = "--levels should be greater than, or equal to 1"
			raise InvalidLevels(message)
	except (TypeError, ValueError):
		message = " ".join([
			"--levels should be an integer and not of type",
			"{}".format(type(args['--levels']))
		])
		raise InvalidLevels(message)

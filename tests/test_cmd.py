from docopt import docopt
from nose.tools import assert_equals

from scrapple import cmd

doc = cmd.__doc__


def test_version():
	args = docopt(doc, "--version")
	assert_equals(args['--version'], True)


def test_genconfig():
	args1 = docopt(doc, "genconfig project1 google.com")
	assert_equals(args1['<projectname>'], 'project1')
	assert_equals(args1['<url>'], 'google.com')
	assert_equals(args1['--type'], 'scraper')
	assert_equals(args1['--selector'], 'xpath')

	args2 = docopt(doc, "genconfig project1 google.com --type=crawler")
	assert_equals(args2['<projectname>'], 'project1')
	assert_equals(args2['<url>'], 'google.com')
	assert_equals(args2['--type'], 'crawler')
	assert_equals(args2['--selector'], 'xpath')

	args3 = docopt(doc, "genconfig project1 google.com -s css")
	assert_equals(args3['<projectname>'], 'project1')
	assert_equals(args3['<url>'], 'google.com')
	assert_equals(args3['--type'], 'scraper')
	assert_equals(args3['--selector'], 'css')

	args4 = docopt(doc, "genconfig project1 google.com -t crawler --selector=css")
	assert_equals(args4['<projectname>'], 'project1')
	assert_equals(args4['<url>'], 'google.com')
	assert_equals(args4['--type'], 'crawler')
	assert_equals(args4['--selector'], 'css')


def test_run():
	args1 = docopt(doc, "run project1 output1")
	assert_equals(args1['<projectname>'], 'project1')
	assert_equals(args1['<output_filename>'], 'output1')
	assert_equals(args1['--output_type'], 'json')

	args2 = docopt(doc, "run project1 output1 -o csv")
	assert_equals(args2['<projectname>'], 'project1')
	assert_equals(args2['<output_filename>'], 'output1')
	assert_equals(args2['--output_type'], 'csv')


def test_generate():
	args1 = docopt(doc, "generate project1 output1")
	assert_equals(args1['<projectname>'], 'project1')
	assert_equals(args1['<output_filename>'], 'output1')
	assert_equals(args1['--output_type'], 'json')

	args2 = docopt(doc, "generate project1 output1 --output_type=csv")
	assert_equals(args2['<projectname>'], 'project1')
	assert_equals(args2['<output_filename>'], 'output1')
	assert_equals(args2['--output_type'], 'csv')

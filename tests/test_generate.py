from nose.tools import assert_is_instance, assert_in
from docopt import docopt
import os

from scrapple import cmd
from scrapple.commands import generate

doc = cmd.__doc__


def test_if_generate_instance_created():
	args = docopt(doc, "generate project1 test_project")
	gc = generate.GenerateCommand(args)
	assert_is_instance(gc, generate.GenerateCommand)


def test_xpath_scraper_generate():
	args = docopt(doc, "generate project1 project")
	gc = generate.GenerateCommand(args)
	gc.execute_command()
	with open(os.path.join(os.getcwd(), 'tests', 'project.py'), 'r') as f:
		program = f.read()
	assert_in("from scrapple.selectors.xpath import XpathSelector", program)
	assert_in('page = XpathSelector("http://www.google.com")', program)


def test_css_scraper_generate():
	args = docopt(doc, "generate project2 project2")
	gc = generate.GenerateCommand(args)
	gc.execute_command()
	with open(os.path.join(os.getcwd(), 'tests', 'project2.py'), 'r') as f:
		program = f.read()
	assert_in("from scrapple.selectors.css import CssSelector", program)
	assert_in('page = CssSelector("http://www.google.com")', program)

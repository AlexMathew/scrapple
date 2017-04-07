import json
import os
import sys
from contextlib import contextmanager

from docopt import docopt
from nose.tools import assert_dict_equal, assert_in, assert_is_instance

from scrapple import cmd
from scrapple.commands import run

doc = cmd.__doc__


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


@contextmanager
def output():
	new_out = StringIO()
	old_out = sys.stdout
	try:
		sys.stdout = new_out
		yield sys.stdout
	finally:
		sys.stdout = old_out


def test_if_run_instance_created():
	args = docopt(doc, "run project1 test_project")
	rc = run.RunCommand(args)
	assert_is_instance(rc, run.RunCommand)


def test_nonexistent_project():
	args = docopt(doc, "run project_unknown project2")
	rc = run.RunCommand(args)
	with output() as out:
		rc.execute_command()
	alert = out.getvalue().strip()
	expected_alert = "project_unknown.json does not exist. Use ``scrapple genconfig``."
	assert_in(expected_alert, alert)


def test_run_xpath_scraper():
	args = docopt(doc, "run project1 result1")
	rc = run.RunCommand(args)
	rc.execute_command()
	with open(os.path.join(os.getcwd(), 'result1.json'), 'r') as f:
		result = json.load(f)
	with open(os.path.join(os.getcwd(), 'expected_result1.json'), 'r') as f:
		expected_result = json.load(f)
	assert_dict_equal(result, expected_result)


def test_run_css_crawler():
	args = docopt(doc, "run project2 result2")
	rc = run.RunCommand(args)
	rc.execute_command()
	with open(os.path.join(os.getcwd(), 'result2.json'), 'r') as f:
		result = json.load(f)
	with open(os.path.join(os.getcwd(), 'expected_result2.json'), 'r') as f:
		expected_result = json.load(f)
	assert_dict_equal(result, expected_result)


def test_run_css_scraper():
	args = docopt(doc, "run project3 result3")
	rc = run.RunCommand(args)
	rc.execute_command()
	with open(os.path.join(os.getcwd(), 'result3.json'), 'r') as f:
		result = json.load(f)
	with open(os.path.join(os.getcwd(), 'expected_result3.json'), 'r') as f:
		expected_result = json.load(f)
	assert_dict_equal(result, expected_result)


def test_run_xpath_crawler():
	args = docopt(doc, "run project4 result4")
	rc = run.RunCommand(args)
	rc.execute_command()
	with open(os.path.join(os.getcwd(), 'result4.json'), 'r') as f:
		result = json.load(f)
	with open(os.path.join(os.getcwd(), 'expected_result4.json'), 'r') as f:
		expected_result = json.load(f)
	assert_dict_equal(result, expected_result)

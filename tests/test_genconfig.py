from nose.tools import assert_equals, assert_list_equal, assert_is_instance
from docopt import docopt
import json
import os

from scrapple import cmd
from scrapple.commands import genconfig

doc = cmd.__doc__


def test_if_genconfig_instance_created():
	args = docopt(doc, "genconfig trial1 http://www.google.com")
	gc = genconfig.GenconfigCommand(args)
	assert_is_instance(gc, genconfig.GenconfigCommand)


def test_if_template_filled():
	args = docopt(doc, "genconfig trial1 http://www.google.com -s css")
	gc = genconfig.GenconfigCommand(args)
	gc.execute_command()
	with open(os.path.join(os.getcwd(), 'trial1.json'), 'r') as f:
		config = json.load(f)
	assert_equals(config['project_name'], "trial1")
	assert_equals(config['selector_type'], "css")
	assert_equals(config['scraping']['url'], "http://www.google.com")


def test_crawler_generation():
	args = docopt(doc, "genconfig trial1 http://www.google.com -t crawler")
	gc = genconfig.GenconfigCommand(args)
	gc.execute_command()
	with open(os.path.join(os.getcwd(), 'trial1.json'), 'r') as f:
		config = json.load(f)
	nextx = [
		{
			"follow_link": "", 
			"scraping": {
				"data": [{"field": "", "selector": "", "attr": "", "default": "", "connector": ""}],
				"table": [
					{
						"table_type": "",
						"header": "",
						"prefix": "",
						"suffix": "",
						"selector": "",
						"attr": "",
						"default": "",
						"connector": ""
					}
				]				
			}
		}
	]
	assert_list_equal(config['scraping']['next'], nextx)

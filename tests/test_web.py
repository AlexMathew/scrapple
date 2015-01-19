from nose.tools import assert_is_instance
from docopt import docopt

from scrapple import cmd
from scrapple.commands import web

doc = cmd.__doc__


def test_if_web_instance_created():
	args = docopt(doc, "web")
	w = web.WebCommand(args)
	assert_is_instance(w, web.WebCommand)

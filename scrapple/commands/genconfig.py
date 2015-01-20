"""
scrapple.commands.genconfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
from jinja2 import Template
import os
import json
from colorama import init, Fore, Back

import scrapple
from scrapple.commands import command

class GenconfigCommand(command.Command):
    """
    Defines the execution of :command: genconfig
    """

    def __init__(self, args):
        self.args = args
        init()

    def execute_command(self):
        """
        Execution method of :command: genconfig
        """
        print(Back.GREEN + Fore.BLACK + "Scrapple Genconfig")
        print(Back.RESET + Fore.RESET)
        directory = os.path.join(scrapple.__path__[0], 'templates', 'configs')
        with open(os.path.join(directory, self.args['--type'] + '.txt'), 'r') as f:
            template_content = f.read()
        print("\n\nUsing the", self.args['--type'], "template\n\n")
        template = Template(template_content)
        settings = {
            'projectname': self.args['<projectname>'],
            'selector_type': self.args['--selector'],
            'url': self.args['<url>']
        }
        rendered = template.render(settings=settings)
        json_content = eval(rendered)
        with open(self.args['<projectname>'] + '.json', 'w') as f:
            json.dump(json_content, f)
        print(Back.WHITE + Fore.RED + self.args['<projectname>'], ".json has been created" \
            + Back.RESET + Fore.RESET, sep="")

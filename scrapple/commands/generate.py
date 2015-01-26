"""
scrapple.commands.generate
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
from jinja2 import Template
import os
import json
from colorama import init, Fore, Back

import scrapple
from scrapple.commands import command

class GenerateCommand(command.Command):
    """
    Defines the execution of :command: generate
    """

    def __init__(self, args):
        self.args = args
        init()

    def execute_command(self):
        """
        Execution method of :command: generate
        """
        print(Back.GREEN + Fore.BLACK + "Scrapple Generate")
        print(Back.RESET + Fore.RESET)
        directory = os.path.join(scrapple.__path__[0], 'templates', 'scripts')
        with open(os.path.join(directory, self.args['--type'] + '.txt'), 'r') as f:
            template_content = f.read()
        print("\n\nUsing the", self.args['--type'], "template\n\n")
        template = Template(template_content)
        try:
            with open(self.args['<projectname>'] + '.json', 'r') as f:
                config = json.load(f)
            config['output_file'] = self.args['<output_filename>']
            rendered = template.render(config=config)
            with open(self.args['<output_filename>'] + '.py', 'w') as f:
                f.write(rendered)
            print(Back.WHITE + Fore.RED + self.args['<output_filename>'], \
                  ".py has been created" + Back.RESET + Fore.RESET, sep="")
        except IOError:
            print(Back.WHITE + Fore.RED + self.args['<projectname>'], ".json does not ", \
                  "exist. Use ``scrapple genconfig``." + Back.RESET + Fore.RESET, sep="")

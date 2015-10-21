"""
scrapple.commands.genconfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
from jinja2 import Template
import os
from colorama import init, Fore, Back

import scrapple
from scrapple.commands import command

class GenconfigCommand(command.Command):
    """
    Defines the execution of :ref:`genconfig <command-genconfig>`
    """

    def __init__(self, args):
        super(GenconfigCommand, self).__init__(args)
        init()

    def execute_command(self):
        """
        The genconfig command depends on predefined `Jinja2 <http://jinja.pocoo.org/>`_ \
        templates for the skeleton configuration files. Taking the --type argument from the \
        CLI input, the corresponding template file is used. 

        Settings for the configuration file, like project name, selector type and URL \
        are taken from the CLI input and using these as parameters, the template is \
        rendered. This rendered JSON document is saved as <project_name>.json.
        
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
            'url': self.args['<url>'],
            'levels': int(self.args['--levels'])
        }
        rendered = template.render(settings=settings)
        with open(self.args['<projectname>'] + '.json', 'w') as f:
            f.write(rendered)
        print(Back.WHITE + Fore.RED + self.args['<projectname>'], ".json has been created" \
            + Back.RESET + Fore.RESET, sep="")

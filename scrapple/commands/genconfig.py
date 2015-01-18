"""
scrapple.commands.genconfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from jinja2 import Template
import os
import json

from . import command

class GenconfigCommand(command.Command):
    """
    Defines the execution of :command: genconfig
    """

    def __init__(self, args):
        self.args = args

    def execute_command(self):
        """
        Execution method of :command: genconfig
        """
        directory = os.path.join(os.getcwd(), 'templates', 'configs')
        with open(os.path.join(directory, self.args['--type'] + '.txt'), 'r') as f:
            template_content = f.read()
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

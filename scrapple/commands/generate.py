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
    Defines the execution of :ref:`generate <command-generate>`
    """

    def __init__(self, args):
        super(GenerateCommand, self).__init__(args)
        init()

    def execute_command(self):
        """
        The generate command uses `Jinja2 <http://jinja.pocoo.org/>`_ templates \
        to create Python scripts, according to the specification in the configuration \
        file. The predefined templates use the extract_content() method of the \
        :ref:`selector classes <implementation-selectors>` to implement linear extractors \
        and use recursive for loops to implement multiple levels of link crawlers. This \
        implementation is effectively a representation of the traverse_next() \
        :ref:`utility function <implementation-utils>`, using the loop depth to \
        differentiate between levels of the crawler execution. 

        According to the --output_type argument in the CLI input, the results are \
        written into a JSON document or a CSV document. 

        The Python script is written into <output_filename>.py - running this file \
        is the equivalent of using the Scrapple :ref:`run command <command-run>`. 

        """
        print(Back.GREEN + Fore.BLACK + "Scrapple Generate")
        print(Back.RESET + Fore.RESET)
        directory = os.path.join(scrapple.__path__[0], 'templates', 'scripts')
        with open(os.path.join(directory, 'generate.txt'), 'r') as f:
            template_content = f.read()
        template = Template(template_content)
        try:
            with open(self.args['<projectname>'] + '.json', 'r') as f:
                config = json.load(f)
            if self.args['--output_type'] == 'csv':
                from scrapple.utils.config import extract_fieldnames
                config['fields'] = str(extract_fieldnames(config))
            config['output_file'] = self.args['<output_filename>']
            config['output_type'] = self.args['--output_type']
            rendered = template.render(config=config)
            with open(self.args['<output_filename>'] + '.py', 'w') as f:
                f.write(rendered)
            print(Back.WHITE + Fore.RED + self.args['<output_filename>'], \
                  ".py has been created" + Back.RESET + Fore.RESET, sep="")
        except IOError:
            print(Back.WHITE + Fore.RED + self.args['<projectname>'], ".json does not ", \
                  "exist. Use ``scrapple genconfig``." + Back.RESET + Fore.RESET, sep="")

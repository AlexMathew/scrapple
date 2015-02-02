"""
scrapple.commands.run
~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
import json
from colorama import init, Fore, Back

from scrapple.commands import command

class RunCommand(command.Command):
    """
    Defines the execution of :command: run
    """

    def __init__(self, args):
        self.args = args

    def execute_command(self):
        """
        Execution method of :command: run
        """
        print(Back.GREEN + Fore.BLACK + "Scrapple Run")
        print(Back.RESET + Fore.RESET)
        try:
            with open(self.args['<projectname>'] + '.json', 'r') as f:
                config = json.load(f)
            
        except IOError:
            print(Back.WHITE + Fore.RED + self.args['<projectname>'], ".json does not ", \
                  "exist. Use ``scrapple genconfig``." + Back.RESET + Fore.RESET, sep="")

        
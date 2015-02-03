"""
scrapple.commands.run
~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
import json
from colorama import init, Fore, Back

from scrapple.commands import command
from scrapple.selectors import xpath, css

class RunCommand(command.Command):
    """
    Defines the execution of :command: run
    """

    def __init__(self, args):
        self.args = args
        init()

    def execute_command(self):
        """
        Execution method of :command: run
        """
        print(Back.GREEN + Fore.BLACK + "Scrapple Run")
        print(Back.RESET + Fore.RESET)
        try:
            with open(self.args['<projectname>'] + '.json', 'r') as f:
                self.config = json.load(f)
            runner = getattr(self, self.args['--type'])
            runner()
        except IOError:
            print(Back.WHITE + Fore.RED + self.args['<projectname>'], ".json does not ", \
                  "exist. Use ``scrapple genconfig``." + Back.RESET + Fore.RESET, sep="")


    def scraper(self):
        selectorClass = getattr(
                eval(self.config['selector_type']), 
                self.config['selector_type'].title() + 'Selector'
                )
        selector = selectorClass(self.config['scraping']['url'])
        return


    def crawler(self):
        selectorClass = getattr(
                eval(self.config['selector_type']), 
                self.config['selector_type'].title() + 'Selector'
                )
        selector = selectorClass(self.config['scraping']['url'])
        return

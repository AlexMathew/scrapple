"""
scrapple.commands.run
~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
import os
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
        results = dict()
        try:
            print()
            print(Back.YELLOW + Fore.BLUE + "Loading page ", self.config['scraping']['url'] \
                + Back.RESET + Fore.RESET)
            selector = selectorClass(self.config['scraping']['url'])
            for attribute in self.config['scraping']['data']:
                if attribute['field'] != "":
                    print("\nExtracting", attribute['field'], "attribute", sep=' ')
                    results[attribute['field']] = selector.extract_content(attribute['selector'], attribute['attr'])
        except Exception, e:
            print(e)
        finally:
            with open(os.path.join(os.getcwd(), self.args['<output_filename>'] + '.json'), 'w') as f:
                json.dump(results, f)
            print()
            print(Back.WHITE + Fore.RED + self.args['<output_filename>'], \
                  ".json has been created" + Back.RESET + Fore.RESET, sep="")


    def crawler(self):
        selectorClass = getattr(
                eval(self.config['selector_type']), 
                self.config['selector_type'].title() + 'Selector'
                )
        selector = selectorClass(self.config['scraping']['url'])
        return

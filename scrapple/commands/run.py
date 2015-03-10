"""
scrapple.commands.run
~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
import os
from colorama import init, Fore, Back

from scrapple.commands import command
from scrapple.selectors import xpath, css
from scrapple.utils.config import traverse_next, extract_fieldnames

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
            import json
            with open(self.args['<projectname>'] + '.json', 'r') as f:
                self.config = json.load(f)
            self.run()
        except IOError:
            print(Back.WHITE + Fore.RED + self.args['<projectname>'], ".json does not ", \
                  "exist. Use ``scrapple genconfig``." + Back.RESET + Fore.RESET, sep="")


    def run(self):
        selectorClass = getattr(
                eval(self.config['selector_type']), 
                self.config['selector_type'].title() + 'Selector'
                )
        results = dict()
        results['project'] = self.args['<projectname>']
        results['data'] = list()
        try:
            result = dict()
            print()
            print(Back.YELLOW + Fore.BLUE + "Loading page ", self.config['scraping']['url'] \
                + Back.RESET + Fore.RESET)
            selector = selectorClass(self.config['scraping']['url'])
            for attribute in self.config['scraping']['data']:
                if attribute['field'] != "":
                    print("\nExtracting", attribute['field'], "attribute", sep=' ')
                    result[attribute['field']] = selector.extract_content(attribute['selector'], attribute['attr'], attribute['default'])
            if not self.config['scraping'].get('next'):
                results['data'].append(result)
            else:
                for next in self.config['scraping']['next']:
                    for r in traverse_next(selector, next, result):
                        results['data'].append(r)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(e)
        finally:
            if self.args['--output_type'] == 'json':
                import json
                with open(os.path.join(os.getcwd(), self.args['<output_filename>'] + '.json'), \
                    'w') as f:
                    json.dump(results, f)
            elif self.args['--output_type'] == 'csv':
                import csv
                with open(os.path.join(os.getcwd(), self.args['<output_filename>'] + '.csv'), \
                    'w') as f:
                    fields = extract_fieldnames(self.config)
                    writer = csv.DictWriter(f, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(results['data'])
            print()
            print(Back.WHITE + Fore.RED + self.args['<output_filename>'], \
                  ".", self.args['--output_type'], " has been created" \
                  + Back.RESET + Fore.RESET, sep="")

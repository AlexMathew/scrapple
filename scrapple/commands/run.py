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
    Defines the execution of :ref:`run <command-run>`
    """

    def __init__(self, args):
        super(RunCommand, self).__init__(args)
        init()

    def execute_command(self):
        """
        The run command implements the web content extractor corresponding to the given \
        configuration file. 

        The execute_command() validates the input project name and opens the JSON \
        configuration file. The run() method handles the execution of the extractor run.

        The extractor implementation follows these primary steps :

        1. Selects the appropriate :ref:`selector class <implementation-selectors>` through \
        a dynamic dispatch, with the selector_type argument from the CLI input. 

        #. Iterate through the data section in level-0 of the configuration file. \
        On each data item, call the extract_content() method from the selector class to \
        extract the content according to the specified extractor rule. 

        #. If there are multiple levels of the extractor, i.e, if there is a 'next' \
        attribute in the configuration file, call the traverse_next() \
        :ref:`utility function <implementation-utils>` and parse through successive levels \
        of the configuration file.

        #. According to the --output_type argument, the result data is saved in a JSON \
        document or a CSV document. 

        """
        try:
            self.args['--verbosity'] = int(self.args['--verbosity'])
            if self.args['--verbosity'] not in [0, 1, 2]:
                raise ValueError
            if self.args['--verbosity'] > 0:
                print(Back.GREEN + Fore.BLACK + "Scrapple Run")
                print(Back.RESET + Fore.RESET)
            import json
            with open(self.args['<projectname>'] + '.json', 'r') as f:
                self.config = json.load(f)
            self.run()
        except ValueError:
            print(Back.WHITE + Fore.RED + "Use 0, 1 or 2 for verbosity." \
                + Back.RESET + Fore.RESET, sep="")
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
            tabular_data_headers = dict()
            if self.args['--verbosity'] > 0:
                print()
                print(Back.YELLOW + Fore.BLUE + "Loading page ", self.config['scraping']['url'] \
                    + Back.RESET + Fore.RESET, end='')
            selector = selectorClass(self.config['scraping']['url'])
            for attribute in self.config['scraping']['data']:
                if attribute['field'] != "":
                    if self.args['--verbosity'] > 1:
                        print("\nExtracting", attribute['field'], "attribute", sep=' ', end='')
                    result[attribute['field']] = selector.extract_content(attribute['selector'], attribute['attr'], attribute['default'])
            if not self.config['scraping'].get('table'):
                result_list = [result]
            else:
                tables = self.config['scraping'].get('table')
                for table in tables:
                    table_headers, result_list = selector.extract_tabular(
                        result=result,
                        table_type=table.get('table_type', 'rows'),
                        header=table.get('header', []),
                        prefix=table.get('prefix', ''),
                        suffix=table.get('suffix', ''),
                        selector=table.get('selector', ''),
                        attr=table.get('attr', 'text'),
                        default=table.get('default', ''),
                        verbosity=self.args['--verbosity']
                        )
                    for th in table_headers:
                        if not th in tabular_data_headers:
                            tabular_data_headers[th] = len(tabular_data_headers)
            if not self.config['scraping'].get('next'):
                results['data'].extend(result_list)
            else:
                for next in self.config['scraping']['next']:
                    for tdh, r in traverse_next(selector, next, result, verbosity=self.args['--verbosity']):
                        results['data'].append(r)
                        for th in tdh:
                            if not th in tabular_data_headers:
                                tabular_data_headers[th] = len(tabular_data_headers)
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
                    data_headers = sorted(tabular_data_headers, key=lambda x:tabular_data_headers[x])
                    fields.extend(data_headers)
                    writer = csv.DictWriter(f, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(results['data'])
            if self.args['--verbosity'] > 0:        
                print()
                print(Back.WHITE + Fore.RED + self.args['<output_filename>'], \
                      ".", self.args['--output_type'], " has been created" \
                      + Back.RESET + Fore.RESET, sep="")

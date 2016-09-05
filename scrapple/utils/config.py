"""
scrapple.utils.config
~~~~~~~~~~~~~~~~~~~~~

Functions related to traversing the configuration file
"""

from __future__ import print_function
from colorama import init, Fore, Back

init()


def traverse_next(page, nextx, results, tabular_data_headers=[], verbosity=0):
    """
    Recursive generator to traverse through the next attribute and \
    crawl through the links to be followed.

    :param page: The current page being parsed
    :param next: The next attribute of the current scraping dict
    :param results: The current extracted content, stored in a dict
    :return: The extracted content, through a generator

    """
    for link in page.extract_links(nextx['follow_link']):
        if verbosity > 0:
            print('\n')
            print(Back.YELLOW + Fore.BLUE + "Loading page ", link.url + Back.RESET + Fore.RESET, end='')
        r = results.copy()
        for attribute in nextx['scraping'].get('data'):
            if attribute['field'] != "":
                if verbosity > 1:
                    print("\nExtracting", attribute['field'], "attribute", sep=' ', end='')
                r[attribute['field']] = link.extract_content(attribute['selector'], attribute['attr'], attribute['default'])
        if not nextx['scraping'].get('table'):
            result_list = [r]
        else:
            tables = nextx['scraping'].get('table')
            for table in tables:
                table_headers, result_list = link.extract_tabular(
                    result=r,
                    table_type=table.get('table_type', 'rows'),
                    header=table.get('header', []),
                    prefix=table.get('prefix', ''),
                    suffix=table.get('suffix', ''),
                    selector=table.get('selector', ''),
                    attr=table.get('attr', 'text'),
                    default=table.get('default', ''),
                    verbosity=verbosity
                    )
                tabular_data_headers.extend(table_headers)
        if not nextx['scraping'].get('next'):
            for r in result_list:
                yield (tabular_data_headers, r)
        else:
            for nextx2 in nextx['scraping'].get('next'):
                for tdh, result in traverse_next(link, nextx2, r, tabular_data_headers=tabular_data_headers, verbosity=verbosity):
                    yield (tdh, result)


def get_fields(config):
    """
    Recursive generator that yields the field names in the config file

    :param config: The configuration file that contains the specification of the extractor
    :return: The field names in the config file, through a generator

    """
    for data in config['scraping']['data']:
        if data['field'] != '': 
            yield data['field']
    if 'next' in config['scraping']:
        for n in config['scraping']['next']:
            for f in get_fields(n): 
                yield f


def extract_fieldnames(config):
    """
    Function to return a list of unique field names from the config file

    :param config: The configuration file that contains the specification of the extractor
    :return: A list of field names from the config file

    """
    fields = []
    for x in get_fields(config):
        if x in fields:
            fields.append(x + '_' + str(fields.count(x) + 1))
        else:
            fields.append(x)
    return fields

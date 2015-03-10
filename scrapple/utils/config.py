"""
scrapple.utils.config
~~~~~~~~~~~~~~~~~~~~~

Functions related to traversing the configuration file
"""

from __future__ import print_function
from colorama import init, Fore, Back

init()


def traverse_next(page, next, results):
    """
    Recursive generator to traverse through the next attribute and \
    crawl through the links to be followed
    """
    for link in page.extract_links(next['follow_link']):
        print(Back.YELLOW + Fore.BLUE + "Loading page ", link.url + Back.RESET + Fore.RESET)
        r = results.copy()
        for attribute in next['scraping'].get('data'):
            if attribute['field'] != "":
                print("\nExtracting", attribute['field'], "attribute", sep=' ')
                r[attribute['field']] = link.extract_content(attribute['selector'], attribute['attr'], attribute['default'])
        if not next['scraping'].get('next'):
            yield r
        else:
            for next2 in next['scraping'].get('next'):
                for result in traverse_next(link, next2, r):
                    yield result


def get_fields(config):
    """
    Recursive generator that yields the field names in the config file
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
    """
    fields = []
    for x in get_fields(config):
        if x in fields:
            fields.append(x + '_' + str(fields.count(x) + 1))
        else:
            fields.append(x)
    return fields

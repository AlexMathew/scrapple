"""
scrapple.utils.config
~~~~~~~~~~~~~~~~~~~~~

Functions related to traversing the configuration file
"""

from __future__ import print_function


def traverse_next(page, next, results):
    """
    Recursive generator to traverse through the next attribute and \
    crawl through the links to be followed
    """
    for link in page.extract_links(next['follow_link']):
        print("Loading page", link.url)
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

"""
Usage:
    scrapple (-h | --help | --version)
    scrapple genconfig <projectname> <url> [--type=<type>] [--selector=<selector>]
    scrapple run <projectname> <output_filename> [--output_type=<output_type>]
    scrapple generate <projectname> <output_filename> [--output_type=<output_type>]
    scrapple web

Options:
    -h, --help
        Show this help message and exit
    --version
        Display the version of Scrapple
    --type=<type>, -t <type>
        Specifies if the script generated is a page scraper or a crawler [default: scraper]
    --selector=<selector>, -s <selector>
        Specifies if XPath expressions or CSS selectors are used [default: xpath]
    --output_type=<output_type>, -o <output_type>
        Specifies if the generated output is stored as CSV or JSON [default: json]
"""

from __future__ import print_function
from docopt import docopt


def run():
    args = docopt(__doc__, version='0.1')


if __name__ == '__main__':
    run()

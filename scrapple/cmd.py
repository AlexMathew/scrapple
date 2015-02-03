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
from operator import itemgetter

from scrapple.utils.dynamicdispatch import get_command_class
from scrapple.utils.exceptions import handle_exceptions


def runCLI():
    args = docopt(__doc__, version='0.1')
    try:
        handle_exceptions(args)
        command_list = ['genconfig', 'run', 'generate', 'web']
        select = itemgetter('genconfig', 'run', 'generate', 'web')
        selectedCommand = command_list[select(args).index(True)]
        cmdClass = get_command_class(selectedCommand)
        obj = cmdClass(args)
        obj.execute_command()
    except Exception as e:
        print('\n', e, '\n')


if __name__ == '__main__':
    runCLI()

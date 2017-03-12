"""
Usage:
    scrapple (-h | --help | --version)
    scrapple genconfig <projectname> <url> [--type=<type>] [--selector=<selector>] \
[--levels=<levels>]
    scrapple run <projectname> <output_filename> [--output_type=<output_type>] \
[--verbosity=<verbosity>]
    scrapple generate <projectname> <output_filename> [--output_type=<output_type>]

Options:
    -h, --help
        Show this help message and exit
    --version, -V
        Display the version of Scrapple
    --type=<type>, -t <type>
        Specifies if the script generated is a page scraper or a crawler [default: scraper]
    --selector=<selector>, -s <selector>
        Specifies if XPath expressions or CSS selectors are used [default: xpath]
    --levels=<levels>, -l <levels>
        Specifies the number of levels for the crawler configuration file [default: 1]
    --output_type=<output_type>, -o <output_type>
        Specifies if the generated output is stored as CSV or JSON [default: json]
    --verbosity=<verbosity>, -v <verbosity>
        Specifies how much of the running is logged. 0 runs the implementation silently; 1 gives basic \
information, like the URL currently being processed; 2 gives a detailed description of the fields being \
extracted [default: 0]
"""

from __future__ import print_function
from docopt import docopt
from operator import itemgetter

from scrapple.utils.dynamicdispatch import get_command_class
from scrapple.utils.exceptions import check_arguments, InvalidType, \
    InvalidSelector, InvalidOutputType, InvalidProjectName, InvalidLevels

POSSIBLE_EXCEPTIONS = (
    InvalidType,
    InvalidSelector,
    InvalidOutputType,
    InvalidProjectName,
    InvalidLevels
)


def runCLI():
    """
    The starting point for the execution of the Scrapple command line tool.

    runCLI uses the docstring as the usage description for the scrapple command. \
    The class for the required command is selected by a dynamic dispatch, and the \
    command is executed through the execute_command() method of the command class.
    """
    args = docopt(__doc__, version='0.3.0')
    try:
        check_arguments(args)
        command_list = ['genconfig', 'run', 'generate']
        select = itemgetter('genconfig', 'run', 'generate')
        selectedCommand = command_list[select(args).index(True)]
        cmdClass = get_command_class(selectedCommand)
        obj = cmdClass(args)
        obj.execute_command()
    except POSSIBLE_EXCEPTIONS as e:
        print('\n', e, '\n')


if __name__ == '__main__':
    runCLI()

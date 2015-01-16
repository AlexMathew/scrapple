from __future__ import print_function
import sys
import argparse
import textwrap

def run():
    parser = argparse.ArgumentParser(
        prog='scrapple',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage='%(prog)s [genconfig | run | generate | web] project_name',
        description=textwrap.dedent(open('files/description.txt').read()),
        epilog=textwrap.dedent(open('files/epilog.txt').read()))
    parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.1')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-v", 
        "--verbose", 
        action="store_true",
        help="Show detailed output"
        )
    group.add_argument(
        "-q", 
        "--quiet", 
        action="store_true",
        help="Show brief output"
        )
    parser.add_argument(
        "action", 
        help=open('files/option_help.txt').read(),
        choices=['genconfig', 'run', 'generate', 'web']
        )
    parser.add_argument(
        "project_name", 
        help=open('files/projectname_help.txt').read(),
        nargs='?',
        default='scrappleproject'
        )
    args = parser.parse_args()

if __name__ == '__main__':
    run()

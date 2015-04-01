.. _implementation-cli:

Command line interface
======================

Scrapple is primarily run through a command line interface. The CLI is used to execute the :ref:`commands supported by Scrapple <framework-commands>`. For a description of the usage of the Scrapple CLI, the help option can be used.

``$ scrapple --help``

This presents the usage description and an explanation of the optional arguments provided by the commands.

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

The ``scrapple`` tool on the command line is included in the system path when Scrapple is :ref:`installed <intro-install>`. When the tool is run, the input on the CLI is parsed by the runCLI() function.

.. autofunction:: scrapple.cmd.runCLI

This functionality is implemented by the following code block -

.. code-block:: python

    handle_exceptions(args)
    command_list = ['genconfig', 'run', 'generate', 'web']
    select = itemgetter('genconfig', 'run', 'generate', 'web')
    selectedCommand = command_list[select(args).index(True)]
    cmdClass = get_command_class(selectedCommand)
    obj = cmdClass(args)
    obj.execute_command()

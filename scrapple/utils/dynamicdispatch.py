"""
scrapple.utils.dynamicdispatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions related to dynamic dispatch of objects
"""

def get_command_class(command):
    """
    Called from runCLI() to select the command class for the selected command.

	:param command: The selected command in the CLI
	:return: The command class corresponding to the selected command
    """
    from scrapple.commands import genconfig, generate, run, web
    cmdClass = getattr(eval(command), command.title() + 'Command')
    return cmdClass

"""
scrapple.utils.dynamicdispatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions related to dynamic dispatch of objects
"""

def get_command_class(command):
    cmdClass = getattr(eval(command), command.title() + 'Command')
    return cmdClass

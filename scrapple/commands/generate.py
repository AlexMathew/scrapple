"""
scrapple.commands.generate
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from . import command

class GenerateCommand(command.Command):
    """
    Defines the execution of :command: generate
    """

    def __init__(self, args):
        self.args = args

    def execute_command(self):
        """
        Execution method of :command: generate
        """
        pass
        
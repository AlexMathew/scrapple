"""
scrapple.commands.run
~~~~~~~~~~~~~~~~~~~~~

"""

from . import command

class RunCommand(command.Command):
    """
    Defines the execution of :command: run
    """

    def __init__(self, args):
        self.args = args

    def execute_command(self):
        """
        Execution method of :command: run
        """
        pass
        
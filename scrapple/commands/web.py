"""
scrapple.commands.web
~~~~~~~~~~~~~~~~~~~~~

"""

from . import command

class WebCommand(command.Command):
    """
    Defines the execution of :command: web
    """

    def __init__(self, args):
        self.args = args

    def execute_command(self):
        """
        Execution method of :command: web
        """
        pass
        
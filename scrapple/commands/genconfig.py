"""
scrapple.commands.genconfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from . import command

class GenconfigCommand(command.Command):
    """
    Defines the execution of :command: genconfig
    """

    def __init__(self, args):
        self.args = args

    def execute_command(self):
        """
        Execution method of :command: genconfig
        """
        pass

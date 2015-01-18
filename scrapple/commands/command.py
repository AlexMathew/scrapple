"""
scrapple.command
~~~~~~~~~~~~~~~~

Contains the definition for the ``Command`` class which provides the basic description of \
the commands used with Scrapple
"""

class Command(object):
    """
    Creates a ``Command`` object, that provides a description of a Scrapple command
    """
    
    def __init__(self, args):
        self.args = args

    def execute_command(self):
        """
        Function for executing the specified command
        """
        raise NotImplementedError

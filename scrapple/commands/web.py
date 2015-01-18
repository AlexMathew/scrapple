"""
scrapple.commands.web
~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
from flask import Flask, render_template
import webbrowser
from multiprocessing import Process

from . import command

class WebCommand(command.Command):
    """
    Defines the execution of :command: web
    """

    app = Flask(__name__)

    def __init__(self, args):
        self.args = args

    def execute_command(self):
        """
        Execution method of :command: web
        """
        p1 = Process(target = lambda : WebCommand.app.run(host="127.0.0.1", port=5000))
        p2 = Process(target = lambda : webbrowser.open('http://127.0.0.1:5000'))
        p1.start()
        p2.start()
        
        
    @app.route('/')
    def home():
        return render_template('home.html')

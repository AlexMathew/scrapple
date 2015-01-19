"""
scrapple.commands.web
~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
from flask import Flask, render_template
import webbrowser
from multiprocessing import Process
from colorama import init, Fore, Back

from scrapple.commands import command

class WebCommand(command.Command):
    """
    Defines the execution of :command: web
    """

    app = Flask(__name__)

    def __init__(self, args):
        self.args = args
        init()

    def execute_command(self):
        """
        Execution method of :command: web
        """
        print(Back.GREEN + Fore.BLACK + "Scrapple Web Interface")
        print(Back.RESET + Fore.RESET)
        p1 = Process(target = lambda : WebCommand.app.run(host="127.0.0.1", port=5000))
        p2 = Process(target = lambda : webbrowser.open('http://127.0.0.1:5000'))
        p1.start()
        p2.start()
        
        
    @app.route('/')
    def home():
        return render_template('home.html')

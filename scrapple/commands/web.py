"""
scrapple.commands.web
~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
from flask import Flask, render_template, request
import webbrowser
from multiprocessing import Process
from colorama import init, Fore, Back

from scrapple.commands import command
from scrapple.utils.form import form_to_json

class WebCommand(command.Command):
    """
    Defines the execution of :ref:`web <command-web>`
    """

    app = Flask(__name__)

    def __init__(self, args):
        super(WebCommand, self).__init__(args)
        init()


    def run_flask(self):
        try:
            WebCommand.app.run(host="127.0.0.1", port=5000)
        except Exception as e:
            import sys
            sys.exit()


    def execute_command(self):
        """
        The web command runs the Scrapple web interface through a simple \
        `Flask <http://flask.pocoo.org>`_ app. 

        When the execute_command() method is called from the \
        :ref:`runCLI() <implementation-cli>` function, it starts of two simultaneous \
        processes : 

        - Calls the run_flask() method to start the Flask app on port 5000 of localhost
        - Opens the web interface on a web browser

        The '/' view of the Flask app, opens up the Scrapple web interface. This \
        provides a basic form, to fill in the required configuration file. On submitting \
        the form, it makes a POST request, passing in the form in the request header. \
        This form is passed to the form_to_json() \
        :ref:`utility function <implementation-utils>`, where the form is converted into \
        the resultant JSON configuration file.

        Currently, closing the web command execution requires making a keyboard interrupt \
        on the command line after the web interface has been closed.

        """
        print(Back.GREEN + Fore.BLACK + "Scrapple Web Interface")
        print(Back.RESET + Fore.RESET)
        p1 = Process(target = self.run_flask)
        p2 = Process(target = lambda : webbrowser.open('http://127.0.0.1:5000'))
        p1.start()
        p2.start()
        
        
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            try:
                form_to_json(request.form)
                return render_template(
                    'complete.html',
                    filename=request.form['project_name']
                    )
            except Exception as e:
                return render_template('error.html', error=e)
        else:    
            return render_template('home.html')

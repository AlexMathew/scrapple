.. _implementation-interaction:

Interaction scenarios
=====================

The primary use cases in Scrapple are the execution of the :ref:`commands <framework-commands>` provided by the framework. A general idea of the execution of these commands and the relation between the various modules of the framework can be understood through a study of the interaction scenarios for each of the commands. 

Basic sequence diagrams for the execution for each command can be represented as such. A more detailed explanation of the execution of the commands is provided in the :ref:`commands implementation <implementation-commands>` section.

.. figure:: images/genconfig.jpg
	:alt: Genconfig sequence diagram
	:align: center

	:ref:`Genconfig command<command-genconfig>`

.. figure:: images/generate.jpg
	:alt: Generate sequence diagram
	:align: center

	:ref:`Generate command<command-generate>`

.. figure:: images/run.jpg
	:alt: Run sequence diagram
	:align: center

	:ref:`Run command<command-run>`

.. figure:: images/web.jpg
	:alt: Web sequence diagram
	:align: center

	:ref:`Web command<command-web>`

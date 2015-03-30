.. _framework-commands:

=================
Scrapple commands
=================

The four commands provided by the Scrapple CLI are

* genconfig
* generate
* run
* web

.. _command-genconfig:

genconfig
---------

The ``genconfig`` command is used to create a skeleton :ref:`configuration file <framework-config>`, which can be used as the base for further writing the necessary configuration file. This makes it easier to understand the structure of the key/value-based configuration file, and provide the necessary options. 

The two positional arguments for the genconfig command are :

- The project name
- The base URL

The ``genconfig`` command creates a basic configuration file with the provided base URL, and creates it as "<project_name>.json".

The two optional arguments for the genconfig command are :

- The type of extractor
- The selector type

The extractor could be a scraper or a crawler, and this can be specified in the --type argument. By default, it is a scraper. When the crawler option is provided, it adds the "next" parameter in the skeleton configuration file. 

With the --selector option, the selector type to be used can be specified. This can be "css" or "xpath". By default, it is "xpath".

Examples :

- ``$ scrapple genconfig pyvideo http://pyvideo.org/category`` creates pyvideo.json, which contains the skeleton configuration file for a scraper which uses XPath expressions as the selector.
- ``$ scrapple genconfig pyvideo http://pyvideo.org/category --type=crawler`` creates pyvideo.json, which contains the skeleton configuration file for a crawler which uses XPath expressions as the selector.
- ``$ scrapple genconfig pyvideo http://pyvideo.org/category --type=crawler --selector=css`` creates pyvideo.json, which contains the skeleton configuration file for a crawler which uses CSS selector expressions as the selector.


.. _command-generate:

generate
--------

The ``generate`` command is used to generate the Python script corresponding to the specifications in the configuration file. This command is used to create the script that replicates the operation of the run command.  

The two positional arguments for the generate command are :

- The project name
- The output file name

The project name is the name of the configuration file to be used, i.e, "<project_name>.json" is the configuration file used as the specification. The command creates "<output_file_name>.py" as the generated Python script.

The one available optional argument is :

- The output type

This specifies the output format in which the extracted content is to be stored. This could be "csv" or "json". By default, it is "json".

Examples :

- ``$ scrapple generate pyvideo talk1`` generates talk1.py based on pyvideo.json, where the extracted data is stored in a JSON document.
- ``$ scrapple generate pyvideo talk1 --output_type=csv`` generates talk1.py based on pyvideo.json, where the extracted data is stored in a CSV document.


.. _command-run:

run
---

The ``run`` command is used to run the extractor corresponding to the specifications in the configuration file. This command runs the extractors and stores the extracted content for later use.  

The two positional arguments for the generate command are :

- The project name
- The output file name

The project name is the name of the configuration file to be used, i.e, "<project_name>.json" is the configuration file used as the specification. The command creates "<output_file_name>.json" or "<output_file_name>.csv" which contains the extracted content.

The one available optional argument is :

- The output type

This specifies the output format in which the extracted content is to be stored. This could be "csv" or "json". By default, it is "json".

Examples :

- ``$ scrapple run pyvideo talk1`` runs the extractor based on pyvideo.json, and stores the extracted content in talk1.json.
- ``$ scrapple run pyvideo talk1 --output_type=csv`` runs the extractor based on pyvideo.json, and stores the extracted content in talk1.csv.


.. _command-web:

web
---

The ``web`` command is an added feature, to make it easier to edit the configuration file. It provides a web interface, which contains a form where the configuration file can be filled. It currently supports only editing configuration files for scrapers. Future work includes support for editing configuration files for link crawlers.

The web interface can be opened with the command

``$ scrapple web``

This starts a Flask web app, which opens on port 5000 on the localhost.

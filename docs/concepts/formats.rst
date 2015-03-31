.. _concepts-formats:

============
Data formats
============

There are several data formats that are used to handle data. This includes XML, CSV, JSON, etc. Scrapple provides support for storing extracted data in two formats :

* Javascript Object Notation (JSON)
* Comma Separated Values (CSV)

JSON
====

Javascript Object Notation (JSON) files are easy to understand and create. They are easy to parse through, understand and write. It is a language independent format and hence many of the APIs use them as a data-interchange format. 

Few data types in JSON are :

* Object: It is an unordered set of name/value pairs. 
* Array: It is a set of values of same data type. It is enclosed in a square bracket and the name-value pairs are separated by a comma. 
* Name: It is the field that describes the data. 
* Value: It is the input data for the name attribute. It can be a number, a Boolean value(true or false), a character(inserted between single quotes) or a string(inserted between double quotes). 

For example,

::

	{

		"subject": "Computer Science",
		"data": [
		# Array

			{	
			# Object

				"name": "John",		# String
				"marks": 96,		# Integer
				"passed": true 		# Boolean

			},

			{

				"name": "Doe",
				"marks": 33,
				"passed": false

			}

		]

	}


CSV
===

Comma Separated Values (CSV) files consists of tabular data where the fields are separated by a comma and the records by a line. It is stored in plain-text format. CSV files are easy to handle and manipulate. 

For example, 

.. csv-table:: 
   :header: Name,Marks,Grade,Promotion
   :widths: 20, 10, 10, 10
   :stub-columns: 1

	John,96,O,True
	Doe,45,F,False

can be represented as,

::

	John,96,O,True
	Doe,45,F,False
	
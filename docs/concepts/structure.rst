.. _concepts-structure:

==================
Web page structure
==================

Structure of a Web page
=======================

The main elements that comprise a web page are :

* DOCTYPE: This lets the browser know the type of markup language the page is written in. 
* Document Tree: We can consider a page as a document tree that contain any number of branches.
* HTML: This is the root element of the document tree and everything that follows is a child node. HTML has two descendants – HEAD and BODY
* HEAD: It contains the title and the information of the page.
* BODY: It contains the data displayed by the page. 

ElementTree
===========

The Element type [6] is a data object that can contain tree-like data structures. 

The ElementTree wrapper [6] type adds code to load web pages as trees of Element objects. 
An element consists of properties like a tag(identify the element type), number of attributes, text string holding the textual content and the number of child nodes. 

To create a tree, we create the root element and add children elements to the root element. A method called Subelement can be used for creating and adding an element to the parent element.
Few methods that are provided to search for Subelements are as follows:

* find(pattern) – Return the first subelement matching the pattern 
* findtext(pattern) – Returns the value of the text attribute of the first subelement matching the pattern
* findall(pattern) – Return a list matching the pattern
* getiterator(tag) - Return a list matching the tag attribute
* getiterator() – Return a list of all the Subelements

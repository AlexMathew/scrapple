.. _intro-tutorials-results:

===================================
Comparison between Scrapple & Ducky
===================================

From the experiments performed with the Scrapple framework, we see that correctly written configuration files give accurate results. In the :ref:`single page linear extractor <intro-tutorials-single-linear>` example and :ref:`link crawler <intro-tutorials-link-crawler>` example (where over 2800 pages were crawled through), an accuracy level of 100% was achieved. 

The accuracy of the implementation of the Scrapple framework is dependent on the user's understanding of :ref:`web structure <concepts-structure>` and the ability to write correct :ref:`selector expressions <concepts-selectors>`. 

On comparison with Ducky [1], it can be seen that Ducky also provides an accuracy of 100%. The primary difference between the Scrapple framework and the Ducky framework is the features provided.

+----------------------------------+------------+------------+
| Feature                          | Scrapple   | Ducky      |
|                                  |            |            |
+==================================+============+============+
| Configuration file               |    YES     |    YES     |
+----------------------------------+------------+------------+
| CSS selectors                    |    YES     |    YES     |
+----------------------------------+------------+------------+
| XPath selectors                  |    YES     |    NO      |
+----------------------------------+------------+------------+
| CSV output                       |    YES     |    YES     |
+----------------------------------+------------+------------+
| JSON output                      |    YES     |    YES     |
+----------------------------------+------------+------------+
| XML output                       |    NO      |    YES     |
+----------------------------------+------------+------------+
| Generation of extractor script   |    YES     |    NO      |
+----------------------------------+------------+------------+



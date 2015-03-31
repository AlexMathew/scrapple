.. _intro-tutorials-results:

===================================
Comparison between Scrapple & Ducky
===================================

From the experiments performed with the Scrapple framework, we see that correctly written configuration files give accurate results. In the :ref:`single page linear extractor <intro-tutorials-single-linear>` example and :ref:`link crawler <intro-tutorials-link-crawler>` example (where over 2800 pages were crawled through), an accuracy level of 100% was achieved. 

The accuracy of the implementation of the Scrapple framework is dependent on the user's understanding of :ref:`web structure <concepts-structure>` and the ability to write correct :ref:`selector expressions <concepts-selectors>`. 

On comparison with Ducky [1]_, it can be seen that Ducky also provides an accuracy of 100%. The primary difference between the Scrapple framework and the Ducky framework is the features provided.

+----------------------------------+------------+------------+
| Feature                          | Scrapple   | Ducky      |
|                                  |            |            |
+==================================+============+============+
| Configuration file               |     ✔      |     ✔      |
+----------------------------------+------------+------------+
| CSS selectors                    |     ✔      |     ✔      |
+----------------------------------+------------+------------+
| XPath selectors                  |     ✔      |     ✘      |
+----------------------------------+------------+------------+
| CSV output                       |     ✔      |     ✔      |
+----------------------------------+------------+------------+
| JSON output                      |     ✔      |     ✔      |
+----------------------------------+------------+------------+
| XML output                       |     ✘      |     ✔      |
+----------------------------------+------------+------------+
| Generation of extractor script   |     ✔      |     ✘      |
+----------------------------------+------------+------------+



.. [1] Kei Kanaoka, Yotaro Fujii and Motomichi Toyama. Ducky: A Data Extraction System for Various Structured Web Documents. In Proceedings of the 18th International Database Engineering & Applications Symposium, IDEAS ’14, pages 342-347, New York, NY, USA, 2014. ACM 


.. _intro-existing:

==========================
Review of existing systems
==========================

Data extraction process from the web can be classified based on the selectors used. Selectors can be CSS or XPath expressions. CSS selectors are said to be faster and are used by many browsers. Ducky [1]_ uses CSS selectors for extracting data from pages that are similarly structured. 

On the other hand, XPath expressions are more reliable, handles text recognition better and a powerful option to locate elements when compared to CSS selectors. Many researches are going on presently in this topic. Oxpath [2]_ provides an extension for XPath expressions. The system created by V. Crescenzi, P. Merialdo, and D. Qiu [3]_ uses XPath expressions for locating the training data to create queries posed to the workers of a crowd sourcing platform. 

Systems like Ducky and Deixto [4]_ use the concept of Configuration files where the user inputs the simple details like base pages, a “next” column if there are multiple pages to be parsed. Deixto uses the concept of tag filtering where the unnecessary html tags can be ignored when the DOM (Document Object Model) tree is created.

Scrapy [5]_, an open source project, provides the framework for web crawlers and extractors. This framework provides support for spider programs that are manually written to extract data from the web. It uses XPath expression to locate the content. The output formats of Ducky and Scrapy include XML, CSV and JSON files.

.. [1] Kei Kanaoka, Yotaro Fujii and Motomichi Toyama. Ducky: A Data Extraction System for Various Structured Web Documents. In Proceedings of the 18th International Database Engineering & Applications Symposium, IDEAS ’14, pages 342-347, New York, NY, USA, 2014. ACM 

.. [2] T.Furche, G.Gottlob, G.Grasso, C.Schallhart, and A.Sellers. Oxpath: A language for scalable data extraction, automation, and crawling on the deep web. The VLDB Journal, 22(1):47–72, Feb. 2013

.. [3] V.Crescenzi, P.Merialdo, and D.Qiu. Alfred: Crowd assisted data extraction. In Proceedings of the 22nd International Conference on World Wide Web Companion, WWW ’13 Companion, pages 297–300, Republic and Canton of Geneva, Switzerland, 2013. International World Wide Web Conferences Steering Committee.

.. [4] F.Kokkoras, K.Ntonas, and N.Bassiliades. Deixto: A web data extraction suite. In Proceedings of the 6th Balkan Conference in Informatics, BCI ’13, pages 9–12, New York, NY, USA, 2013. ACM.

.. [5] `Scrapy <https://www.scrapy.org>`_: A fast and powerful scraping and web crawling framework.
 
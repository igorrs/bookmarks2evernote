bookmarks2evernote
==================

A simple command line tool to transform bookmarks exported from Google Chrome and Google Bookmarks into Evernote as individual notes using EN's enex format.
If the html file you are using as input uses H3 as folder name, this are translated into Evernote tags. For this to work correctly, you must ensure when exporting Google Chrome Bookmarks that all the folders are located at the end of your bookmark's list.

It also indentifies duplicated bookmarks in the same HTML file. Google Bookmarks export feature duplicates all bookmarks with more than one tag.

Requisites:
-----------

* Python
* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). An excellent python library for html parsing and navigation. Follow their instructions for installation.

Usage:
------
It takes a single parameter, the name of the input html file. The ouput file will have the same name but with an enex extension.

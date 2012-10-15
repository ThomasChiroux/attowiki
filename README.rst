attowiki
========

attowiki is a very small wiki engine for personal use.

It's main features are:

* can be started in any directory
* uses all .rst files in directory structure as "wiki" files
* uses git for revision control
* automatic background saving
* added 2 new directives: 'todo' and 'done'
* some meta pages, including:

  * */__index__*: gives a list of all meta pages and normal pages
  * */__todo__*: gives a list of all todo found in all pages
  * */__cheatsheet__*: docutils reStructuredText cheat sheet

usage
-----

Launching a wiki

::

    $ attowiki

that's all.

attowiki will start a small server
(by default, serving to http://localhost:8080)

all the .rst files inside the current directory will be used for the wiki


installation
------------

::

    $ pip install attowiki


project dependencies
""""""""""""""""""""

* bottle
* docutils
* gitpython


attowiki
========

attowiki is a very small wiki engine for personal use.

Its main features are:

* can be started in any directory
* uses all .rst files in directory structure as "wiki" files
* uses git for revision control
* automatic background saving
* history view of old version of pages, including source and diff views
* added 2 new directives: 'todo' and 'done'
* some meta pages, including:

  * */__index__*: gives a list of all meta pages and normal pages
  * */__cheatsheet__*: docutils reStructuredText cheat sheet

  * */__todo__*: gives a list of all todo found in all pages
  * */__done__*: gives a list of all done found in all pages
  * */__xxxxxxx__*: gives a list of all *xxxxxxx* found in all pages, *xxxxxxx*
    represent any reStructure *node*, like all admonitions:

    * __todo__
    * __done__
    * __attention__
    * __caution__
    * __danger__
    * __error__
    * __hint__
    * __important__
    * __note__
    * __tip__
    * __warning__
    * __admonition__

  * "admonition" meta pages for one page only
    using this kind of url: /name of the doc.__admonitionname__

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


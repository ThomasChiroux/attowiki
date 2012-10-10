========
attowiki
========

attowiki is a very small wiki engine for personal use.

It's main functions are:

* can be started in any directory
* uses all .rst files in directory structure as wiki files
* uses git for revision control

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

project dependencies
""""""""""""""""""""

* bottle
* docutils
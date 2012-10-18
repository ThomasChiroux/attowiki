Version History
---------------

current
"""""""

* added static file serving as fall back (and 404 still fall back of static files-
  It's useful when a reST doc tries to include local files (like images), which
  are now server by attowiki

* Bug Corrections

  * git history was not available when serving attowiki in a subdir of a git repo

v0.4
""""

* added a 'view diff' button when viewing a previous version of a file
* added a 'view source' button when viewing a previous version of a file
* added an history view of previous versions of a file
* added __todo__ meta page which scan all the directory for todo directives
  and display it in one page
* added more generic __xxxxxxxx__ meta page which scan all the directory
  for the xxxxxxxx admnonition. This may work with any registered node,
  especially admonitions:

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

* added possibility to use the "admonition" meta pages for one page only
  using this kind of url: /name of the doc.__admonition_name__

* added __cheatsheet__ meta page which provides locally a docutils reST
  cheatsheet
* added 'done' directive, in order to work with todo: when a task is done,
  edit the page and change 'todo' to 'done' (it will remove it from
  __todo__ meta page)
* removed iframe
* improved docutils css
* some other refactors

v0.3
""""

* added todo directive support in rest files (now display correctly a todo)
* changed a little bit the default docutils css
* added background saving feature

v0.2
""""

* start in a dir, looks for .rst files and serve them in html
* looks for index.rst at first and serve it
* if index.rst not found serve a page with the list of files
* simple edition (text area). Save and Cancel buttons
* git commit when saving


v0.1
""""

* first (non-working) version
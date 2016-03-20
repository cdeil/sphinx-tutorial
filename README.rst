Sphinx tutorial
===============

What is this?
+++++++++++++

* A one hour `Sphinx <http://www.sphinx-doc.org/>`__ tutorial introduction.
* By `Christoph Deil <https://github.com/cdeil>`__ and `Stuart Mumford <https://github.com/cadair>`__ .
* March 21, 2016 at `PyAstro16 <http://python-in-astronomy.github.io/2016/>`__ .

You will learn how to add Sphinx documentation to a Python package (using the
example ``astrospam`` Python package in this repo). The focus is exclusively on
technical aspects how to work with Sphinx. We will **not** have time to talk
about how to write good documentation, i.e. what content to create and how to
structure it.

You are encouraged to follow along, i.e. try out every step on your computer
after we demo it.

**If you have a question, or something isn't working for you, or if I'm going too
fast, please feel free to interrupt me at any time!**

If we run out of time, we will do the last two sections (5. Autodoc and 6. Theme)
as a demo. I.e. you'll watch us do them and then, if you like, do them
yourself on your own time after the tutorial.

Overview
++++++++

1. `Introduction <https://gist.github.com/cdeil/1ec8b694aea3952f5267#1-introduction>`__
2. `Installation <https://gist.github.com/cdeil/1ec8b694aea3952f5267#2-installation>`__
3. `Quickstart <https://gist.github.com/cdeil/1ec8b694aea3952f5267#3-quickstart>`__
4. `RST <https://gist.github.com/cdeil/1ec8b694aea3952f5267#4-RST>`__
5. `Autodoc <https://gist.github.com/cdeil/1ec8b694aea3952f5267#5-autodoc>`__
6. `Theme <https://gist.github.com/cdeil/1ec8b694aea3952f5267#6-theme>`__
7. `Final comments <https://gist.github.com/cdeil/1ec8b694aea3952f5267#7-final-comments>`__


0. TODO
-------

* Write and improve notes for most steps
* Add lots of little exercises for each step

1. Introduction
---------------

TODO: start directly by describing the ``astrospam`` example package.


We'll start with a quick overview of Sphinx and related things by having a
look at the following web pages.

* We won't talk about `this Sphinx <https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Great_Sphinx_of_Giza_-_20080716a.jpg/800px-Great_Sphinx_of_Giza_-_20080716a.jpg>`_.
* `Wikipedia on Sphinx (documentation generator) <https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)>`__
* http://www.sphinx-doc.org/, especially the
  `Sphinx tutorial <http://www.sphinx-doc.org/en/stable/tutorial.html>`__
  and the `reStructuredText Primer <http://www.sphinx-doc.org/en/stable/rest.html>`__
* https://en.wikipedia.org/wiki/ReStructuredText
* http://www.sphinx-doc.org/en/stable/man/sphinx-apidoc.html
* https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
* http://www.sphinx-doc.org/en/stable/ext/napoleon.html
* https://readthedocs.org/
* Examples of projects using Sphinx (almost all Python projects do):
  `Python <https://docs.python.org/3/>`__
  `Astropy <http://astropy.readthedocs.org/en/latest/>`__,
  `Astroplan <http://astroplan.readthedocs.org/>`__

If you want to learn more, please go back and read the info on those pages
after the tutorial on your own.

For now, let's go ahead with our hands-on introduction to Sphinx and
start using it ...

2. Installation
---------------

Open a terminal and type ``sphinx<TAB>``. If this lists ``sphinx-*`` commands
(e.g ``sphinx-quickstart`` or ``sphinx-build``), you have Sphinx installed.
Type ``sphinx-build --version`` to check the Sphinx version number.

The latest stable version is 1.3.
If you have 1.2 or older, I'd suggest you update now e.g. using::

    $ pip install --upgrade sphinx
    $ conda install sphinx

Later on we'll use the `sphinx_rtd_theme <https://github.com/snide/sphinx_rtd_theme>`__ .
Please install it now via::
    
    $ pip install sphinx_rtd_theme


3. Quickstart
-------------

Let's say you have a Python project consisting of a few ``.py`` files,
and would like to use Sphinx to generate HTML or PDF documentation for it.

As an example for today's tutorial, please grab this repo:

    $ git clone https://github.com/cdeil/sphinx-tutorial
    $ cd sphinx-tutorial

As you can see, there is a Python package called ``astrospam``:

    $ tree .
    TODO


sphinx-quickstart
+++++++++++++++++

sphinx-build
++++++++++++

* Run ``sphinx-quickstart docs``
* Run ``cd docs && make html``
* ``make latexpdf``

4. RST
------



* Add some content on ``index.rst`` page.
* Add a sub-page ``tutorial.rst`` and some more content there.
* TODO: something that causes a Sphinx warning
* TODO: something that causes a Sphinx error

5. Autodoc
----------

Add a simple module ``pyastro16.py`` with the following content:


TODO: link from docstrings to docs in RST file and the other way around.

Note that Sphinx autodoc imports the Python module and accesses
docstrings stored in ``__doc__`` attributes. This means that
module-level and class-level code is executed.

TODO: Illustrate by adding print statements.
TODO: Add code that throws an exception (e.g. ``import spam`` or ``1/0`` or a ``SyntaxError``)
and show the resulting Sphinx error message.

Explain about `__all__`

6. Theme
--------

TODO: show how to change to the readthedocs template and what changes.

7. Final comments
-----------------

* We hope that this tutorial gave you a basic understanding of what Sphinx is,
  how it works, and how you use it to generate the documentation for Python
  projects.
* You should now be able to contribute to the documentation of existing
  Python projects and maybe even be able to set up Sphinx for your own
  package (e.g. by copy & pasting the working `package-template <https://github.com/astropy/package-template>`__ setup).
* There's many things we didn't cover that will come up if you start contributing
  to Sphinx documentation for projects like Astropy or Astropy-affiliated packages:
  plot directive, setup.py integration, doctests, ...
* Sphinx, like other documentation generators such as LaTeX or Doxygen, is a
  very complicated, and extremely extensible and customisable tool.
  Even with years of experience you can easily get stuck with an uncomprehensible
  error message and get frustrated.
  Don't be shy to ask for help!

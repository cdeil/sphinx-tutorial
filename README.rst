Sphinx tutorial
===============

What is this?
+++++++++++++

* A one hour `Sphinx <http://www.sphinx-doc.org/>`__ tutorial introduction.
* By `Christoph Deil <https://github.com/cdeil>`__ and `Stuart Mumford <https://github.com/cadair>`__ .
* March 21, 2016 at `PyAstro16 <http://python-in-astronomy.github.io/2016/>`__ .

You will learn how to add Sphinx documentation to a Python package (using the
example ``astrospam`` Python package in this repo).

The focus is exclusively on technical aspects how to work with Sphinx. We will
**not** have time to talk about how to write good documentation, i.e. what
content to create and how to structure it.

You are encouraged to follow along, i.e. try out every step on your computer
after we demo it.

Before we start:

* Who has run Sphinx before (i.e. run ``sphinx-build`` or ``make html`` or ``python setup.py build_sphinx``)?
* Who has set up Sphinx before (i.e. run ``sphinx-quickstart``, edited ``docs/conf.py``)?

**If you have a question, or something isn't working for you, or if I'm going too
fast, please feel free to interrupt us at any time!**

Overview
++++++++

1. `Introduction <https://gist.github.com/cdeil/1ec8b694aea3952f5267#1-introduction>`__
2. `Installation <https://gist.github.com/cdeil/1ec8b694aea3952f5267#2-installation>`__
3. `Quickstart <https://gist.github.com/cdeil/1ec8b694aea3952f5267#3-quickstart>`__
4. `RST <https://gist.github.com/cdeil/1ec8b694aea3952f5267#4-RST>`__
5. `Autodoc <https://gist.github.com/cdeil/1ec8b694aea3952f5267#5-autodoc>`__
6. `Theme <https://gist.github.com/cdeil/1ec8b694aea3952f5267#6-theme>`__
7. `Final comments <https://gist.github.com/cdeil/1ec8b694aea3952f5267#7-final-comments>`__

1. Introduction
---------------

We'll start with a quick overview of Sphinx and related things by having a
look at the following web pages.

If you want to learn more, please go back and read the info on those pages
after the tutorial on your own.

* We won't talk about `this Sphinx <https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Great_Sphinx_of_Giza_-_20080716a.jpg/800px-Great_Sphinx_of_Giza_-_20080716a.jpg>`_.
  (I don't know why the Sphinx documentation generator was given that name.)
* To get some basic info on Sphinx, read the
  `Wikipedia on Sphinx (documentation generator) <https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)>`__
  or the welcome page of the Sphinx website at http://www.sphinx-doc.org/ .
* The most useful pages in the Sphinx documentation to get started are the
  `Sphinx tutorial <http://www.sphinx-doc.org/en/stable/tutorial.html>`__
  and the `reStructuredText Primer <http://www.sphinx-doc.org/en/stable/rest.html>`__
* Almost all Python projects use reStructured text (RST) and Sphinx for documentation.
  Examples: `Python <https://docs.python.org/3/>`__
  `Astropy <http://astropy.readthedocs.org/en/latest/>`__,
  `Astroplan <http://astroplan.readthedocs.org/>`__
* As the `Wikipedia article on reStructuredText (RST) <https://en.wikipedia.org/wiki/ReStructuredText>`__
  explains, RST is a markup language (like LaTeX or Markdown) that is mostly used for Python docstrings (in ``.py`` files)
  and high-level documentation (in ``.rst`` files).
* Sphinx is the tool that takes RST as input and produces HTML or PDF as output.
  To be more precise, Sphinx is a Python package that is mostly used via the command line tools
  ``sphinx-quickstart`` and ``sphinx-build`` (which again you typically invoke via a ``Makefile``).
* `Python docstrings <https://en.wikipedia.org/wiki/Docstring#Python>`__ are extracted by
  the Sphinx "autodoc" feature to auto-generate API (application programming interface) docs.
  There's a few different formats for docstrings in use that Sphinx supports.
* The one all scientific Python packages (Numpy, Scipy, Astropy, ...) use is called the
  `Numpy docstring standard <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>`__
  which as added as a built-in Sphinx extension called
  `sphinx.ext.napoleon <http://www.sphinx-doc.org/en/stable/ext/napoleon.html>`__
  (I don't know why it was called Napoleon.)
* Once documentation is set up for your package, it's typically easy to generate HTML
  output by just running ``make html`` which calls ``sphinx-build``,
  or by executing ``python setup.py build_sphinx`` which runs the Sphinx build.
  Then you can look at the output by just opening up ``index.html`` in some output
  directory where the HTML docs have been generated.
  Working on documentation is then a matter of editing ``.rst`` or ``.py`` files,
  running ``make html`` and checking the HTML output or console for errors and warnings.
* Finally, if you want to host the generated HTML, the free https://readthedocs.org/
  and https://pages.github.com/ services are good options.
  We won't have time to cover those today, feel free to ask us after if you want to
  learn how they work or want help to set it up for your project.

Let's go ahead with our hands-on introduction to Sphinx and start using it ...

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

Before we continue, everyone please check that you're set up::
    
    $ sphinx-build --version
    Sphinx (sphinx-build) 1.3.6
    $ python -c 'import sphinx_rtd_theme'
    # Should give no output.
    # If you get an ImportError, `sphinx_rtd_theme` isn't installed correctly.

3. Quickstart
-------------

Let's say you have a Python project consisting of a few ``.py`` files,
and would like to use Sphinx to generate HTML or PDF documentation for it.

Example package
+++++++++++++++

As an example for today's tutorial, please grab this repo::

    $ git clone https://github.com/cdeil/sphinx-tutorial
    $ cd sphinx-tutorial

As you can see, there is a Python package called ``astrospam``::

    $ tree .
    .
    ├── LICENSE
    ├── README.rst
    └── astrospam
        ├── __init__.py
        ├── ham.py
        ├── pyastro16.py
        └── spam.py

You can import and use it::

    $ python
    >>> import astrospam
    >>> astrospam.spam()
    Spam
    Spam
    Spam
    >>> exit()

But there's no HTML documentation for it. Let's change that!

sphinx-quickstart
+++++++++++++++++

To add Sphinx documentation, you run `sphinx-quickstart <http://www.sphinx-doc.org/en/stable/invocation.html#invocation>`__

This will prompt you for some information and then generate a few of files.

For most questions you can just hit ``ENTER`` to accept the default. These are
the questions where you don't take the default, but actually put something::
    
    $ sphinx-quickstart

    Welcome to the Sphinx 1.3.6 quickstart utility.

    > Root path for the documentation [.]: docs
    > Project name: astrospam
    > Author name(s): Astrospam developers
    > Project version: 0.1
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y

    Finished: An initial directory structure has been created.

The tool created the following files:

* ``docs/conf.py`` -- Sphinx configuration file
* ``docs/index.rst`` -- Name of your master docs page
* ``docs/Makefile`` -- Makefile as convenience to run Sphinx (for Linux and Mac OS X)
* ``docs/make.bat`` -- Makefile for Windows

And the following empty directories:

* ``docs/_build`` -- This is where all output files (e.g. HTML) will go when Sphinx runs.
* ``docs/_static`` -- A place for static files, e.g. images or css (we won't use it)
* ``docs/_templates`` -- A place for template files (we won't use it)


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

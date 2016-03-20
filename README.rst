Sphinx tutorial
===============

These are the notes for a beginner `Sphinx <http://www.sphinx-doc.org/>`__
tutorial  given by `Christoph Deil <https://github.com/cdeil>`__ on March 21,
2016 at `PyAstro16 <http://python-in-astronomy.github.io/2016/>`__ .

The goal is to get you up and running with Sphinx, i.e. the technical know-how
to generate documentation for Python projects. We will **not** have time to talk
about how to write good documentation, i.e. what content to create and how to
structure it.

You are encouraged to follow along, i.e. try out every step on your computer
after I demo it.

If you have a question, or something isn't working for you, or if I'm going too
fast, please feel free to interrupt me at any time!

Overview:

1. `Introduction <https://gist.github.com/cdeil/1ec8b694aea3952f5267#1-introduction>`__
2. `Installation <https://gist.github.com/cdeil/1ec8b694aea3952f5267#2-installation>`__
3. `Quickstart <https://gist.github.com/cdeil/1ec8b694aea3952f5267#3-quickstart>`__
4. `RST <https://gist.github.com/cdeil/1ec8b694aea3952f5267#4-RST>`__
5. `Autodoc <https://gist.github.com/cdeil/1ec8b694aea3952f5267#5-autodoc>`__
6. `Theme <https://gist.github.com/cdeil/1ec8b694aea3952f5267#6-theme>`__
7. `Plots <https://gist.github.com/cdeil/1ec8b694aea3952f5267#7-plots>`__
8. `setup.py integration <https://gist.github.com/cdeil/1ec8b694aea3952f5267#8-setuppy-integration>`__
9. `Doctests <https://gist.github.com/cdeil/1ec8b694aea3952f5267#9-doctests>`__
10. `Final comments <https://gist.github.com/cdeil/1ec8b694aea3952f5267#10-final-comments>`__


It's hard to say how far we'll get within the given time. Sections 1 to 4 are
the basics. It would be good if we get to cover Sections 5 and 6. Sections 7 to
10 are optional, no worries if we don't get ot those.

0. TODO
-------

* Add lots of little exercises
* Post on Github as ``sphinx-tutorial``
* Add final version to the repo? Intermediate versions?

1. Introduction
---------------

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

* Readthedocs template

7. Plot directive
-----------------

TODO: give example
Explain how it works and how it's usually the 

8. setup.py integration
-----------------------

Astropy, affiliated packages and some other Python packages have integrated
Sphinx as a subcommand in ``setup.py``, i.e. instead of running
``cd docs && make html`` developers should run ``python setup.py build_sphinx``.

TODO: comments on ``sys.path``

As the last step, let's make edits to the Sphinx documentation of a
large Python project: Astropy.

Clone https://github.com/astropy/astropy and make two docs edits:

* ``docs/coordinates/index.rst`` --- what?
* ``astropy/coordinates/angle.py`` -- what?

Run ``python setup.py build_sphinx`` and explain how to check the result.


9. Doctests
-----------

Sphould we cover doctests

10. Final comments
------------------

* We hope that this tutorial gave you a basic understanding of what Sphinx is,
  how it works, and how you use it to generate the documentation for Python
  projects.
* You should now be able to contribute to the documentation of existing
  Python projects and maybe even be able to set up Sphinx for your own
  package (e.g. by copy & pasting the working `package-template <https://github.com/astropy/package-template>`__ setup).
* Sphinx, like other documentation generators such as LaTeX or Doxygen, is a
  very complicated, and extremely extensible and customisable tool.
  Even with years of experience you can easily get stuck with an uncomprehensible
  error message and get frustrated.
  Don't be shy to ask for help!

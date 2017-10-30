.. ###########################################################################
   This file contains reStructuredText, please do not edit it unless you are
   familar with reStructuredText markup as well as Sphinx specific markup.

   For information regarding reStructuredText markup see
      http://sphinx.pocoo.org/rest.html

   For information regarding Sphinx specific markup see
      http://sphinx.pocoo.org/markup/index.html

.. ########################## SECTION HEADING REMINDER #######################
   # with overline, for parts
   * with overline, for chapters
   =, for sections
   -, for subsections
   ^, for subsubsections
   ", for paragraphs

.. ---------------------------------------------------------------------------

************
Introduction
************

This documentation serves as a set of notes for the developer and a record of
the implementation for those individuals who wish to better understand the
implmentation details of this fork of `Cookiecutter Repo on GitHub`_ in order to
implement a new **cookeicutter.json** format spec as proposed by
`hackebrot's cookiecutter pull request #848`_.


Cookiecutter References
=======================

The following are useful Cookiecutter references:

   * `ReadTheDocs`_
   * `Cookiecutter Repo on GitHub`_
   * `hackebrot's cookiecutter pull request #848`_ - the catalyst for this implementation effort


Timeline
========
The initial implementation & test of this work was done over the course of
8 days between 20 Oct and 28 Oct 2017. After 100% test coverage was attained,
the code was re-visited due to an implementation defect in the handling of
**extra context** overwrites -- it needed to be more sophisticated for v2 contexts.
The defect resolution was attained on 29 Oct 2017 with 100% test coverage;
however, more tests were added on 30 Oct 2017 to cover all **extra context**
overwrites for each type of field supported in the v2 context.


.. _hackebrot's cookiecutter pull request #848: https://github.com/audreyr/cookiecutter/pull/848
.. _ReadTheDocs: http://cookiecutter.readthedocs.io/en/latest/readme.html
.. _Cookiecutter Repo on GitHub: https://github.com/audreyr/cookiecutter


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

.. _testing-section:

*******
Testing
*******

The baseline v1.6.0 test run in the :ref:`Setup section <baseline_test_run>` showed totals of::

   =================== 260 passed, 1 skipped in 25.54 seconds ===============

The v2.0.0 test run below shows the following totals::

   =================== 307 passed, 1 skipped in 38.97 seconds =================

So thus far, 47 tests have been added::

                       v1.6.0  v2.0.0    Delta   Delta
                        Tests   Tests    Tests     %
         Test Totals     261     308      47    +18.0%


The following new test files & test support directories:

   **tests/test_generate_context_v2.py** - Tests v2 changes made to **generate.py**.

   **tests/test-generate-context-v2/** - Contains test support files for **tests/test_generate_context_v2.py**.

   **tests/test_context.py** - Tests new file **context.py**.

   **tests/test-context/** - Contains test support files for **tests/test_context.py**.

Test coverage for v2.0.0 looks like this::

   ----------- coverage: platform win32, python 3.6.2-final-0 -----------
   Name                          Stmts   Miss  Cover   Missing
   -----------------------------------------------------------
   cookiecutter\__init__.py          2      0   100%
   cookiecutter\__main__.py          3      0   100%
   cookiecutter\cli.py              49      0   100%
   cookiecutter\config.py           51      0   100%
   cookiecutter\context.py         161      0   100%       <--- new file
   cookiecutter\environment.py      21      0   100%
   cookiecutter\exceptions.py       24      0   100%
   cookiecutter\extensions.py        9      0   100%
   cookiecutter\find.py             18      0   100%
   cookiecutter\generate.py        222      0   100%       <--- modified file
   cookiecutter\hooks.py            61      1    98%   95
   cookiecutter\log.py              21      0   100%
   cookiecutter\main.py             34      0   100%       <--- modified file
   cookiecutter\prompt.py           90      0   100%
   cookiecutter\replay.py           30      0   100%
   cookiecutter\repository.py       39      0   100%
   cookiecutter\utils.py            50      0   100%
   cookiecutter\vcs.py              54      0   100%
   cookiecutter\zipfile.py          61      2    97%   10-11
   -----------------------------------------------------------
   TOTAL                          1000      3    99%

   =================== 307 passed, 1 skipped in 38.97 seconds =================


Also to improve the test coverage report, an additional option was added to
the **pytest** section of the **set.cfg** file.

The git diff looks like this::

   $ git diff setup.cfg
   diff --git a/setup.cfg b/setup.cfg
   index 83901b4..805cc52 100644
   --- a/setup.cfg
   +++ b/setup.cfg
   @@ -16,5 +16,5 @@ universal = 1

    [tool:pytest]
    testpaths = tests
   -addopts = --cov=cookiecutter
   +addopts = --cov-report term-missing --cov=cookiecutter

This additional **'--cov-report term-missing'** option adds the *Missing*
column to the test coverage report so you can easily determine what lines of
code are missing coverage.

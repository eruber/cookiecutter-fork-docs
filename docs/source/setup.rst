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

**************************
Dev/Test Environment Setup
**************************
The following sections detail the sets taken to get a development and test
environment configured to establish a testing baseline.

Primary development and testing was done using::

      Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34)
      [MSC v.1900 32 bit (Intel)] on win32

Some **Posix** testing was also done as described in the next section.

Notes Regarding Development Console Sessions
============================================
Note that two different consoles are used on **Windows 10** (which is the source
of most documented console sessions in this document):

   1. The `git-bash <https://git-scm.com>`_ console uses a **$** prompt
   2. The `ConEmu <https://conemu.github.io>`_ console session uses a **>** prompt

On **Posix** a `Virtual Box`_ system running `Ubuntu Desktop`_ **16.04.3 LTS**
on a **Windows 10** host was used to run unit tests and do adhoc command line testing.


Development/Test Environment Setup
==================================
The following steps were taken to setup the initial development & test environment:

1. Fork the `Cookiecutter Repo on GitHub`_ to the `Cookiecutter Version 2 Project on GitHub`_
2. Clone the forked repo to local development machine, create a development branch
   and check it out::

      $ cd /d/Devel/_python/__eru/___forks/
      $ git clone https://github.com/eruber/cookiecutter.git
      $ cd cookiecutter
      $ git checkout -b new-2.0-context

3. Create a virtual environment for development and test::

      > cd D:\Devel\_python\__eru\___forks\cookiecutter
      > python -m venv .env

   We chose **.env** because that directory is defined in the **.gitignore**
   file.

4. Activate the virtual environment & list pre-installed packages::

      >.env\Scripts\activate.bat
      (.env) >pip list

      Package    Version
      ---------- -------
      pip        9.0.1
      setuptools 28.8.0


5. Install **cookicutter** in development (editable) mode & list cookiecutter's
   installed dependencies::

      (.env) >pip install -e .

      (.env) >pip list

      Package         Version     Location
      --------------- ----------- --------------------------------------------
      arrow           0.10.0
      binaryornot     0.4.4
      certifi         2017.7.27.1
      chardet         3.0.4
      click           6.7
      cookiecutter    1.6.0       d:\devel\_python\__eru\___forks\cookiecutter
      future          0.16.0
      idna            2.6
      Jinja2          2.9.6
      jinja2-time     0.2.0
      MarkupSafe      1.0
      pip             9.0.1
      poyo            0.4.1
      python-dateutil 2.6.1
      requests        2.18.4
      setuptools      28.8.0
      six             1.11.0
      urllib3         1.22
      whichcraft      0.4.1

6. Install test requirements & list installed packages::

      (.env) >pip install -r test_requirements.txt

      (.env) >type test_requirements.txt
      pytest
      pytest-cov
      pytest-mock==1.1
      pytest-catchlog
      freezegun

      (.env) >pip list
      Package         Version     Location
      --------------- ----------- --------------------------------------------
      arrow           0.10.0
      binaryornot     0.4.4
      certifi         2017.7.27.1
      chardet         3.0.4
      click           6.7
      colorama        0.3.9
      cookiecutter    1.6.0       d:\devel\_python\__eru\___forks\cookiecutter
      coverage        4.4.1
      freezegun       0.3.9
      future          0.16.0
      idna            2.6
      Jinja2          2.9.6
      jinja2-time     0.2.0
      MarkupSafe      1.0
      pip             9.0.1
      poyo            0.4.1
      py              1.4.34
      pytest          3.2.3
      pytest-catchlog 1.2.2
      pytest-cov      2.5.1
      pytest-mock     1.1
      python-dateutil 2.6.1
      requests        2.18.4
      setuptools      28.8.0
      six             1.11.0
      urllib3         1.22
      whichcraft      0.4.1


7. Run pytest (the **setup.cfg** file configures pytest to run from the project root)::

      (.env) D:\Devel\_python\__eru\___forks\cookiecutter>pytest
      ============================= test session starts ========================
      platform win32 -- Python 3.6.2, pytest-3.2.3, py-1.4.34, pluggy-0.4.0
      rootdir: D:\Devel\_python\__eru\___forks\cookiecutter, inifile: setup.cfg
      plugins: mock-1.1, cov-2.5.1, catchlog-1.2.2
      collected 261 items

      tests\test_abort_generate_on_hook_error.py ..
      tests\test_cli.py ...........................
      tests\test_cookiecutter_invocation.py ..
      tests\test_cookiecutter_local_no_input.py .......
      tests\test_cookiecutter_local_with_input.py ..
      tests\test_custom_extensions_in_hooks.py ..
      tests\test_default_extensions.py .
      tests\test_environment.py ..
      tests\test_exceptions.py .
      tests\test_find.py ..
      tests\test_generate_context.py ..........
      tests\test_generate_copy_without_render.py .
      tests\test_generate_file.py .....
      tests\test_generate_files.py ..................
      tests\test_generate_hooks.py ...s....
      tests\test_get_config.py .....
      tests\test_get_user_config.py .........
      tests\test_hooks.py ..........
      tests\test_log.py ...
      tests\test_main.py ..
      tests\test_output_folder.py ..
      tests\test_preferred_encoding.py .
      tests\test_prompt.py .........................
      tests\test_read_repo_password.py .
      tests\test_read_user_choice.py .....
      tests\test_read_user_dict.py .......
      tests\test_read_user_variable.py .
      tests\test_read_user_yes_no.py .
      tests\test_repo_not_found.py .
      tests\test_specify_output_dir.py ..
      tests\test_utils.py .........
      tests\replay\test_dump.py .....
      tests\replay\test_load.py ....
      tests\replay\test_replay.py ......
      tests\repository\test_abbreviation_expansion.py .......
      tests\repository\test_determine_repo_dir_clones_repo.py .....
      tests\repository\test_determine_repo_dir_finds_existing_cookiecutter.py .
      tests\repository\test_determine_repository_should_use_local_repo.py ...
      tests\repository\test_is_repo_url.py .............
      tests\repository\test_repository_has_cookiecutter_json.py ...
      tests\vcs\test_clone.py ..........
      tests\vcs\test_identify_repo.py .............
      tests\vcs\test_is_vcs_installed.py ....
      tests\zipfile\test_unzip.py .............


      ----------- coverage: platform win32, python 3.6.2-final-0 -----------
      Name                          Stmts   Miss  Cover
      -------------------------------------------------
      cookiecutter\__init__.py          2      0   100%
      cookiecutter\__main__.py          3      0   100%
      cookiecutter\cli.py              49      0   100%
      cookiecutter\config.py           51      0   100%
      cookiecutter\environment.py      21      0   100%
      cookiecutter\exceptions.py       24      0   100%
      cookiecutter\extensions.py        9      0   100%
      cookiecutter\find.py             18      0   100%
      cookiecutter\generate.py        166      0   100%
      cookiecutter\hooks.py            61      1    98%
      cookiecutter\log.py              21      0   100%
      cookiecutter\main.py             31      0   100%
      cookiecutter\prompt.py           90      0   100%
      cookiecutter\replay.py           30      0   100%
      cookiecutter\repository.py       39      0   100%
      cookiecutter\utils.py            50      0   100%
      cookiecutter\vcs.py              54      0   100%
      cookiecutter\zipfile.py          61      2    97%
      -------------------------------------------------
      TOTAL                           780      3    99%


      =================== 260 passed, 1 skipped in 25.54 seconds ===============



.. _baseline_test_run:

At this point, we have a working test environment based on Cookiecutter v1.6.0;
therefore test development and implementation work can begin.

To compare these baseline test numbers to the v2.0.0 test numbers go to the :ref:`testing-section` section.

.. _Cookiecutter Version 2 Project on GitHub: https://github.com/eruber/cookiecutter
.. _Cookiecutter Repo on GitHub: https://github.com/audreyr/cookiecutter
.. _Virtual Box: https://www.virtualbox.org/wiki/Downloads
.. _Ubuntu Desktop: https://www.ubuntu.com/desktop

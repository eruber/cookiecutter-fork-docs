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

*****
Tools
*****
In the course of doing this implementation a couple of utitlity tools were
developed and are presented herein.

Context Dump Utility
====================
This utility allows one to play with different **cookiecutter.json** and see
what context variables are produced without actually doing any jinja2
rendering of files.

This very same functionality could be easily attained using cookiecutter if
the command line interface supported a --dumpcontext option.

contextdump.py
--------------
Usage: contextdump.py [OPTIONS]

  Load the specified json object from the --cct PATH and if --no-input is
  omitted, prompt the user for input. After all input is gathered, the
  template's context is dumped.

Options:
  --cct PATH  Path to a Cookiecutter template file (cct), defaults to
              'cookiecutter.json'
  --no-input  Do not prompt for parameters and only use cookiecutter.json file
              content
  --tdump     If specified, dump the  input Cookiecutter template file
              specified by the --cct PATH option
  -h, --help  Show this message and exit.

Requires an environment that includes a cookiecutter installation.


Template Transformer
====================
This utility will convert a version 1 **cookiecutter.json** file to version 2.

The original **cookiecutter.json** file will be renamed cookiecutter_v1.json and
the transformed version 2 file will become **cookiecutter.json**.

templatetransformer.py
----------------------

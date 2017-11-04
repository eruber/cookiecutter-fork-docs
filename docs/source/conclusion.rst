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

**********
Conclusion
**********
Apologies for the length of this document, but it helped me clarify my thoughts
as I progressed through the implementation. Most things don't seem all that
complicated from afar, but when you start looking at them with a microscope,
you can get shoulder's deep in no time. Write ups help me deal with complexity.

It is obvious from the discussion in `hackebrot's cookiecutter pull request #848`_
that the Cookiecutter maintainers and community feel that adding v2 context support
is a fairly risky thing that will certainly increase the overall support effort.
Those sentiments are definitely valid from my perspective as well.

This whole digression for me snowballed gradually and then gained momentum
simply because I wanted a "skip_if" feature and I was so impressed by
hachebrot's **context.py** code.

Another apology for not include Python 2.7 support as per the Contributor
Guidelines -- I honestly lack the ergs to do it now -- I suspect the issues
are more with the tests than with the application code -- but quite honestly,
for me Python 2.7 is a blip on the horizon in my rear-view mirror. However,
I do want to make the pull request available regardless, to generate some
discussion and feedback. Perhaps it will ulitmately lead to something positive
for the **Cookiecutter** community.

As menioned in the introduction, I have a repo `here`_ containing a command
line tool that will convert a version 1 template to a version 2 template.
I of course will not deploy it to PyPI since it would, no doubt, cause all
sorts of confusion. But it is available for experimentation.

Anyway, I shall submit my pull request now... if anyone actually read this far,
I am impressed with your fortitude.


.. _hackebrot's cookiecutter pull request #848: https://github.com/audreyr/cookiecutter/pull/848
.. _here: https://github.com/eruber/cookiecutter-template-converter

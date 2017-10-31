# -*- coding: utf-8 -*-

"""
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

"""
import codecs
import pprint
import collections
import json

from cookiecutter.context import load_context

import click


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.option(
    '--cct', default='cookiecutter.json', type=click.Path(),
    help="Path to a Cookiecutter template file (cct), defaults to 'cookiecutter.json'"
)
@click.option(
    '--no-input', is_flag=True, default=False,
    help='Do not prompt for parameters and only use cookiecutter.json file content',
)
@click.option(
    '--tdump', is_flag=True, default=False,
    help='If specified, dump the  input Cookiecutter template file specified '
         'by the --cct PATH option')
def main(cct, no_input, tdump):
    """
    Load the specified json object from the --cct PATH and if --no-input is
    omitted, prompt the user for input. After all input is gathered, the
    template's variable context is dumped.
    """

    with codecs.open(cct, 'r', encoding='utf8') as f:
        json_object = json.load(f, object_pairs_hook=collections.OrderedDict)

    if tdump:
        with codecs.open(cct, 'r', encoding='utf8') as t:
            template = t.readlines()

        template = [line.rstrip() for line in template]

        width, _ = click.get_terminal_size()
        click.echo("Cookiecutter Template File: '{cctf}'".format(cctf=cct))
        for line in template:
            click.echo(line)

        click.echo('-' * (width - 5))

    context = load_context(json_object, no_input, False)

    click.echo("Context Dump:")
    pprint.pprint(context, indent=4, width=190)


if __name__ == '__main__':
    main()

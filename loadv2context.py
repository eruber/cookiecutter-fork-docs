# -*- coding: utf-8 -*-

"""
v2 cookiecutter context dumper
------------------------------

"""
import codecs
import pprint
import collections
import json

from cookiecutter.context import load_context

import click


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.option(
    '--json-file', default='cookiecutter.json', type=click.Path(),
    help="Path to a Cookiecutter v2 template file, defaults to 'cookiecutter.json'"
)
@click.option(
    '--no-input', is_flag=True,
    help='Do not prompt for parameters and only use cookiecutter.json file content',
)
def main(json_file, no_input):
    """Load the json object and prompt the user for input"""

    with codecs.open(json_file, 'r', encoding='utf8') as f:
        json_object = json.load(f, object_pairs_hook=collections.OrderedDict)

    context = load_context(json_object, no_input, False)
    pprint.pprint(context, indent=4, width=190)


if __name__ == '__main__':
    main()

import os
import click
from click import echo
from clint.textui import indent, puts, prompt

@click.command('register', short_help='perform image registration', options_metavar='<options>')
def register():
    print 'performing image registration'

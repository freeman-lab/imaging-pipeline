import click

settings = dict(help_option_names=['-h', '--help'])
from .commands import register

@click.group(options_metavar='', subcommand_metavar='<command>', context_settings=settings)
def cli():
    """
    Welcome to imaging-pipeline! This is a command line tool for processing 
    calcium imaging data, built out of modular components.

    If you're just getting started, call 'imaging-pipeline --help' 
    """
    pass

cli.add_command(register)
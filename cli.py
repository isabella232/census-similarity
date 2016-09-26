import logging

import click

from census_similarity import commands


@click.group()
def cli():
    """Command Line Interface for census similarity"""
    logging.basicConfig(level=logging.DEBUG)


cli.add_command(commands.cluster_by_field)


if __name__ == '__main__':
    cli()
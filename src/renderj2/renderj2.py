#!/usr/bin/env python3
from logging import getLogger
from pathlib import Path

import click
import click_log
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from renderj2 import PACKAGE_NAME, __version__

logger = getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click.help_option("-h", "--help")
@click.version_option(__version__, "-V", "--version", package_name=PACKAGE_NAME)
@click.option(
    "-v",
    "--varsfile",
    type=click.Path(exists=True),
    multiple=True,
    help="vars file path for jinja2",
)
@click.argument("template_file", type=click.Path(exists=True))
@click_log.simple_verbosity_option(logger, "--loglevel", show_default=True)
def cmd(template_file: str, varsfile: list[str]) -> None:
    """
    Rendre Jinja2 tempalte
    """
    template_path = Path(template_file)
    env = Environment(
        loader=FileSystemLoader(template_path.parent, encoding="utf8"),
        autoescape=select_autoescape(),
    )
    logger.debug(f"Load template file [{template_path}]")

    template = env.get_template(template_path.name)

    vars_dict: dict[str, str] = {}
    for filename in varsfile:
        logger.debug(f"Load vars file [{filename}]")
        filepath = Path(filename)
        with filepath.open() as fd:
            yaml_dict = yaml.safe_load(fd)
            vars_dict.update(yaml_dict)
    logger.debug(f"Used vars dict {vars_dict}")
    click.echo(template.render(vars_dict))

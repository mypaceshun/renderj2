#!/usr/bin/env python3

import click
import yaml


@click.command()
@click.option('-v', '--varsfile',type=click.File('r'), multiple=True,
              help='vars file path for jinja2')
@click.argument('template', type=click.File('r'))
def cmd(template, varsfile):

    print(template.name)
    for line in template:
        print(line)

    for var in varsfile:
        print(var.name)
        data = yaml.load(var)
        print(data)

def main():
    cmd()

if __name__ == '__main__':
    main()

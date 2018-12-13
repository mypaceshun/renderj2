#!/usr/bin/env python3

import click


@click.command()
@click.option('-v', '--varsfile',type=click.File('r'), multiple=True,
              help='vars file path for jinja2')
@click.argument('template', type=click.File('r'),
                help='retemplate file path for jinja2')
def cmd(template, varsfile):
    print(template)
    print(varsfile)

def main():
    cmd()

if __name__ == '__main__':
    main()

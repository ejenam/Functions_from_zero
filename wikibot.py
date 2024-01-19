from mylib.bot import scrape
import click

@click.command()
@click.option('--name',
              help='web page we want to scrape')
@click.option('--length',
              help='length of the output from wikipedia')
def cli(name, length=1):
    result = scrape(name, length)
    click.echo(click.style(f"{result}", fg="red"))

if __name__ == '__main__':
    cli()
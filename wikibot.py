from mylib.bot import scrape
import click


@click.command()
@click.option("--name", default="microsoft", help="web page we want to scrape")
@click.option("--length", default=1, help="length of the output from wikipedia")
def cli(name, length):
    # pylint: disable=no-value-for-parameter
    result = scrape(name, length)
    click.echo(click.style(f"{result}", fg="red"))


if __name__ == "__main__":
    cli()

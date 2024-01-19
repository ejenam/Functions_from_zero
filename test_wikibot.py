from mylib.bot import scrape
from wikibot import cli
from click.testing import CliRunner

def test_scrape():
    assert 'Microsoft' in scrape('microsoft')

def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Microsoft', '--length', 2])
    assert result.exit_code == 0
    assert 'Microsoft' in result.output
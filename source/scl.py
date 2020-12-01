import click
import requests
import json
from tabulate import tabulate


@click.command()
@click.option('--section', help='What you want to see?  Just type the section')
@click.argument('section')
def get(section):

    """
    Simple CLI for accessing sathyabama latest updates

    """

    """This return a particular topic from sathyabama site [like news and events]"""


    url_format = 'https://sathyabama-api.herokuapp.com/{}'
    # click.echo(id)

    response = requests.get(url_format.format(section))
    if not response:
        click.echo('Section is not yet available.')
    else:
        if section=='news':
            table = make_table(response)
            print(tabulate(table, headers=["News Title", "Details"],
                    tablefmt="fancy_grid"))

        elif section=='events':
            table = make_table1(response)
            print(tabulate(table, headers=["Event Title", "Details"],
                    tablefmt="psql"))
            tabulate.options.display.max_columns = None
        

    # click.echo(response.json())

def make_table(response):
    res = response.json()
    result = []
    for item in res["list"]:
        new = []
        new.append(item['News'])
        new.append((item['Time']))
        result.append(new)
    for item in res["list"]:
        new = []
        new.append('[Read More]: ' + item['URL'])
        result.append(new)

    return result

def make_table1(response):
    res = response.json()
    
    result = []
    for item in res["list"]:
        new = []
        new.append(item['Event'][:40] + "\n" + item['Event'][40:75] + "...")
        new.append(item['Time'] + '\n' + item['Venue'])
        new.append(item['URL'][:35] + '\n' + item['URL'][35:80] + '\n' + item['URL'][80:])
        result.append(new)

    return result


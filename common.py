import requests

from settings import click_url


def send_trigger(resource):
    print 'A ' + resource + ' was occurred!'
    url = click_url + '/' + resource
    try:
        requests.get(url=url)
    except:
        print 'Server not found url :: ' + url


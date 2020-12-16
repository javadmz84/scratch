import requests

from bs4 import BeautifulSoup


def get_site(url):
    data = requests.get(url)
    return data


def make_soup(data):
    soup = BeautifulSoup(data.text, 'html.parser')
    return soup


def get_tag(soup, name, cls):
    tags = soup.find_all(name,  class_=cls)
    return tags


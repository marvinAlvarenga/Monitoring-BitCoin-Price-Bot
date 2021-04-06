import requests
import schedule
from bs4 import BeautifulSoup

from environment import BASE_URL


def send_request(url):
    return requests.get(url)


def buil_request(message):
    return BASE_URL + message


def send_message(message):
    url = buil_request(message)
    send_request(url)


if __name__ == '__main__':
    send_message('Hola soy marvin!')

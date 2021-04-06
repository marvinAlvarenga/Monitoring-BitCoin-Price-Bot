import requests
import schedule
from bs4 import BeautifulSoup

from environment import BASE_URL, BIT_COIN_URL


def send_request(url):
    return requests.get(url)


def buil_request(message):
    return BASE_URL + message


def send_message(message):
    url = buil_request(message)
    send_request(url)


def get_bit_coin_price():
    response = send_request(BIT_COIN_URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})

    return result.text


def report_bit_coin_price():
    btc_price = get_bit_coin_price()

    message = f'The current price of Bit Coin is: {btc_price}'
    send_message(message=message)


def schedule_report():
    schedule.every().minute.at(':00').do(report_bit_coin_price)


if __name__ == '__main__':
    schedule_report()

    while True:
        schedule.run_pending()

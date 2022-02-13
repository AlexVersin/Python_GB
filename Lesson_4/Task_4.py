import sys

import utils

url1 = "http://www.cbr.ru/scripts/XML_daily.asp"
currency1 = input("Введи код валюты: ")

if __name__ == "__main__":
    print(utils.currency_rates(url1, currency1))
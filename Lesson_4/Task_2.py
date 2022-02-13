from requests import get, utils

url1 = "http://www.cbr.ru/scripts/XML_daily.asp"
currency1 = input("Введи код валюты: ")

def currency_rates(url, currency):
    url = get(url)
    currency = currency.upper() # Сделать работу функции не зависящей от того, в каком регистре был передан аргумент.
    encodings = utils.get_encoding_from_headers(url.headers)
    content = url.content.decode(encoding=encodings) #Запрос контента с сервера

    if currency not in content: #Проверка условия - Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть объект None.
        return None

    value = content.split(currency)[1].split("</Value>")[0].split("<Value>")[1]  #Вычленение значенеи из строки url
    value_symbol = value.find(",")                                              # Перевод строки в число с запятой
    value = float(value[0 : (value_symbol)] + "." + value[(value_symbol+1):])   # Перевод строки в число с запятой
    return value

print(currency_rates(url1, currency1))
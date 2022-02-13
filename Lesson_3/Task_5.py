#Импорт рандома для смешного вывода
from random import randint
#Заданные списки
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

#Функция возврата строк-шуток
def get_jokes(range_1, nouns, adverbs, adjectives):
    list_1 = []     #Создание пустого списка
    l = 0       #Счетчик строк пустой
    while l <= range_1:
        random_nouns = randint(0, len(nouns) - 1)   #Выбор случайного слова из списка nouns
        random_adverbs = randint(0, len(adverbs) - 1)   #Выбор случайного слова из списка adverbs
        random_adjectives = randint(0, len(adjectives) - 1)     #Выбор случайного слова из списка adjectives
        list_1.append(nouns[random_nouns] + " " + adverbs[random_adverbs] + " " + adjectives[random_adjectives])    #Формирование списка строк
        l += 1      #Счетчик строк
    return list_1       #Функция возвращает список строк

print(get_jokes(3, nouns, adverbs, adjectives)) #Вывод на экран список строк шуток:)

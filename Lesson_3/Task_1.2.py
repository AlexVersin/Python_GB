# Решение задания:
def num_translate(word):
    word_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре",
                 "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь",
                 "nine": "девять", "ten": "десять"}
    return word_dict.get(word)
#Вывод на экран
print(num_translate("two"))
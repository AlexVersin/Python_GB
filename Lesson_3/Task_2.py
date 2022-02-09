def num_translate_adv(word):
    word_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре",
                 "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь",
                 "nine": "девять", "ten": "десять"}
    if word in word_dict:
        return word_dict.get(word)

    elif word.lower() in word_dict:
        a = word.lower()
        a = word_dict.get(a)
        return a.capitalize()

print(num_translate_adv("ten"))
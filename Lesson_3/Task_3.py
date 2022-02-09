#Решение задания
def thesaurus(*args):
    sort_args = sorted(args)
    dict_name = {}
    for l in sort_args:
        key = l[0]
        if key not in dict_name:
            dict_name[key] = []
        dict_name[key].append(l)
    return dict_name

print(thesaurus("Кирилл", "Алекс", "Иван", "Мария", "Петр", "Илья", "Юден", "Юля", "Иан"))
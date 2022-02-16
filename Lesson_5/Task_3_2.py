def iterator_with_yield(tutor, group):
    att = 0
    while tutor:
        try:
            if group[att] in group:
                add_group = group[att]
        except IndexError:
            add_group = None
        yield (tutor[att], add_group)
        att+=1

#Результат, где учеников меньше
#tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
#groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

#Результат, где учеников больше
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
groups = ['9А', '7В', '9Б', '9В']

print("Ученики:", tutors)
print("Классы:", groups)
gen1 = iterator_with_yield(tutors, groups)
print("Тип объекта:", type(gen1))
print("Все значения генератора:")
for x in gen1:
    print(x)
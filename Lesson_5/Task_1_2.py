# Создание генератора сделайте внутри функции iterator_without_yield(n),
# примающей аргументом n любое положительное число и возвращающей генератор
def iterator_without_yield(n):
    nums_gen = (num for num in range(1, n+1, 2))
    return nums_gen


gen1 = iterator_without_yield(11)
for x in gen1:
    print(x)
print(next(gen1))
# gen1 = iterator_without_yield(11)
#next(gen1) = 1
#next(gen1) = 3 и т.д до 11
# Истощал генератор в консоли получил верный вывод "StopIteration"
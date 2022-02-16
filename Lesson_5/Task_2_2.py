# Создание генератора сделайте внутри функции iterator_with_yield(n),
# примающей аргументом n любое положительное число и возвращающей генератор
def iterator_with_yield(n):
    start = 1
    step = 2
    last_nums = start
    while start <= n:
        yield start, last_nums
        start += step
        last_nums = last_nums + start


gen1 = iterator_with_yield(14)
for x in gen1:
    print(x)
print(next(gen1))
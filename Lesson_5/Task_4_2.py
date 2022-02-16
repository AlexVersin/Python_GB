#Обычная запись
from time import perf_counter

start = perf_counter()

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for x in src:
    a_index = src.index(x)-1
    a = src[a_index]
    if x > a:
        result.append(x)
print(result, perf_counter() - start)

#Comprehensions запись
start = perf_counter()

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [x for x in src if x > src[(src.index(x)-1)]]
print(result, perf_counter() - start)
from time import perf_counter

start = perf_counter()
src = [2, 2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
junk = []
for x in src:
    if x not in junk:
        if x not in result:
            result.append(x)
        elif x in result:
            if x not in junk:
                junk.append(x)
                result.remove(x)
            elif x in junk:
                result.remove(x)
print(result, perf_counter() - start)

#Насколько эффективен такой код?
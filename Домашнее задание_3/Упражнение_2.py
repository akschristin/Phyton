#Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
a = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(a)
c = []
for i in a:
    if i % 2 == 0:
        c.append(a.index(i))
        print(i, end=' ')
print(c, end='  ')
# В В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
a = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(a)

n = 0
x = 0
for i in range(SIZE):
   if a[i] < a[n]:
        n = i
   elif a[i] > a[x]:
        x = i
print('a[%d]=%d a[%d]=%d' % (n+1, a[n], x+1, a[x]))
b = a[n]
a[n] = a[x]
a[x] = b

for i in range(SIZE):
    print(a[i], end='  ')
print()






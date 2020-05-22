# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

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

if n > x:
    n, x = x, n
s = 0
for i in range(n+1, x):
    s = s + a[i]
print(f'Сумма элементов между мин и макс числами: ', s)
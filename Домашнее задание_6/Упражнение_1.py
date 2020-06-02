# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Условия задачи к упражнению 3 урока задания 1: В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

#X86-64, Python 3.8

# 1 вариант
import sys
for h in range(2,10):
    c = []
    for i in range(2,100):
         if i % h == 0:
            c.append(i)
    print(f'{h} - {len(c)}')

sum_size = 0
sum_size += sys.getsizeof(h)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(c)

print('Переменные занимают', sum_size, 'байт') #Переменные занимают 120 байт.

# 2 вариант
import sys
MIN_ITEM_1 = 2
MAX_ITEM_1 = 99
MIN_ITEM_2 = 2
MAX_ITEM_2 = 9
for i in range(MIN_ITEM_2, MAX_ITEM_2 + 1):
    num = 0
    for j in range(MIN_ITEM_1, MAX_ITEM_1 + 1):
        if j % i == 0:
            num += 1
    print(f'{i} кратны {num} числа')

sum_size = 0
sum_size += sys.getsizeof(MIN_ITEM_1)
sum_size += sys.getsizeof(MAX_ITEM_1)
sum_size += sys.getsizeof(MIN_ITEM_2)
sum_size += sys.getsizeof(MAX_ITEM_2)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(num)
sum_size += sys.getsizeof(j)

print('Переменные занимают', sum_size, 'байт') #Переменные занимают 98 байт. Вариант решения задачи № 2 более оптимальный,
# так как под переменные отводится меньшее количество памяти по сравнению с двумя другими вариантами решения.

# 3 вариант
import sys
MIN_ITEM_1 = 2
MAX_ITEM_1 = 99
MIN_ITEM_2 = 2
MAX_ITEM_2 = 9
num = [0] * (MAX_ITEM_2 - MIN_ITEM_2 + 1)
for i in range(MIN_ITEM_1, MAX_ITEM_1 + 1):
    for j in range(MIN_ITEM_2, MAX_ITEM_2 + 1):
        if i % j == 0:
            num [j - MIN_ITEM_2] += 1

for i, item in enumerate(num, start=MIN_ITEM_2):
    print(f'{i} кратны {item} числа')

sum_size = 0
sum_size += sys.getsizeof(MIN_ITEM_1)
sum_size += sys.getsizeof(MAX_ITEM_1)
sum_size += sys.getsizeof(MIN_ITEM_2)
sum_size += sys.getsizeof(MAX_ITEM_2)
sum_size += sys.getsizeof(num)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(j)
sum_size += sys.getsizeof(item)

print('Переменные занимают', sum_size, 'байт') #Переменные занимают 158 байт
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

A = int(input('Введите количество строк: '))
B = int(input('Введите количество столбцов: '))
matrix = []

for i in range(A):
    f = []
    for j in range(B):
        f.append(int(input('Введите число в строку: ')))
    matrix.append(f)


for i in range(A):
    for j in range(B):
        print(matrix[i][j], end = ' ')
    print()

matrix_1 = []
for i in range(A):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(B - 1):
        n = int(input())
        s = s + n
        b.append(n)
    b.append(s)
    matrix_1.append(b)

for i in matrix_1:
    print(i)

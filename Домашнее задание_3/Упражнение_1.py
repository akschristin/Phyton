# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [i for i in range(2, 100)]
b = [h for h in range(2, 10)]
c = []
for h in range(2,10):
    c = []
    for i in range(2,100):
         if i % h == 0:
            c.append(i)
    print(f'{h} - {len(c)}: {c}')


N = int(input('Введите размер списка: '))
A = [int(s) for s in input('Введите элементы списка: ').split()]
X = int(input('Введите число x: '))
k = 0
for i in range(N):
    if A[i] == X:
        k += 1
print(k)


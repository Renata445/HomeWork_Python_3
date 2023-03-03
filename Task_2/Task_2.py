N = int(input('Введите размер списка: '))
A = [int(s) for s in input('Введите элементы списка: ').split()]
X = int(input('Введите число X: '))
min = abs(X - A[0])
index = 0
for i in range(N):
    count = abs(X - A[i])
    if count < min:
        min = count
        index = i
print(A[index])
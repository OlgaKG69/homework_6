a1 = int(input("Введите значение 1-го элемента:"))
d = int(input("Введите разность элементов:"))
n = int(input("Введите количество элементов:"))
for i in range(n):
    print(a1 + i * d, end=' ')

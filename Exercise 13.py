x = int(input("Введите целое число X: "))
y = int(input("Введите целое число Y: "))
result = 1 if x % y == 0 or y % x == 0 else 2
print(result)

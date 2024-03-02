bitcoin = input('Введите стоимость биткоина в рублях: ')
price = str(bitcoin)
index = len(price) - 3
if 0 <= index < len(price):
    digit = price[index]
    print('Цифра на третьей позиции справа:', digit)
else:
    print('В числе меньше трех символов')
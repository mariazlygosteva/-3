x, y, n = map(int, input('Введите цену за чашку латте (рубли и копейки) и количество заказов: ').split())
kopecks = (x * 100 + y) * n
rubles = kopecks // 100
kopecks = kopecks % 100
print(rubles, 'руб.', kopecks, 'коп.')

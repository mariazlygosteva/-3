n = float(input('Введите количество градусов, на которое повернулась часовая стрелка: '))
hours = int(n // 30)
minutes = int((n % 30) / 30 * 60)
print('Полных часов прошло с начала суток: ', hours)
print('Полных минут прошло с начала суток: ', minutes)
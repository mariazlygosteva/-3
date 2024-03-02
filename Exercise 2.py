time = int(input('Введите количество секунд от 1 до 86400: '))

if time < 1 or time > 86400:
    print('Введенное число должно быть от 1 до 86400')
else:
    hour = time // 3600
    minute = (time % 3600) // 60
    second = time % 60

    print('Текущее время:', hour, 'часов', minute, 'минут', second, 'секунд')

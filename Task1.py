number = int(input('Введите количество секунд: '))

sec = number % 60
minutes = number % 3600 // 60
hours = number % 86400 // 3600
days = number // 86400

print(days, 'дн.', hours, 'час.', minutes, 'мин.', sec, 'сек.')

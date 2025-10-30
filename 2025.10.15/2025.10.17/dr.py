from datetime import datetime, timedelta
print(datetime.now())
birthday = datetime(1974, 6, 12, 10, 25)
print('Прошло ', datetime.now() - birthday)
print(birthday + timedelta(10000))
print(birthday.strftime('%Y.%m.%d %H:%M'))
exam = datetime.strptime(
    '2025.09.25 19:30', '%Y.%m.%d %H:%M')
print(birthday.year)

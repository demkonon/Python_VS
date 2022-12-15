# Считается, что Вы знаете, что такое високосный год
# (делится на 4 и не делится на 100 или делится на 400)
# Считается, что Вы знаете, сколько дней в каждом месяце
# Считается известным, что в неделе 7 дней


# 1. Сегодня вторник, 13-е декабря 2022 года
# Используя только эту информацию вычислить день недели нового года.
# Подсказка: правильный ответ: воскресенье

# 2. Есть ли годы, начинающиеся с пн? со вт?
# Привести ближайший пример.

# 3. В какой день недели Вы родились? Перечислить все свои ДР,
# пришедшиеся на тот же день недели.

class Year_self:

    def __init__(self):
        self.__sum_days = None

    def day_in_year(self, yr_u, yr_v, td, wk):
        self.__year_u = yr_u
        self._year_v = yr_v
        self.__today_m = td
        self.__week_m = wk
        enter_date = input('day/month/year:').split('/')
        if enter_date[2] % 4 != 0 and enter_date[2] % 100 == 0:
            for m in self.__year_u.values():
                for i in m:
                    self.__sum_days += i[0]
        return self.__sum_days
    















y_s = Year_self()
print(y_s.day_in_year(year_us, year_v, today_m, week_m))

year_us = {
    'January': [31, 1],
    'February': [28, 2],
    'March': [31, 3],
    'April': [30, 4],
    'May': [31, 5],
    'June': [30, 6],
    'July': [31, 7],
    'August': [31, 8],
    'September': [30, 9],
    'October': [31, 10],
    'November': [30, 11],
    'December': [31, 12] 
}
year_v = {
    'January': [31, 1],
    'February': [29, 2],
    'March': [31, 3],
    'April': [30, 4],
    'May': [31, 5],
    'June': [30, 6],
    'July': [31, 7],
    'August': [31, 8],
    'September': [30, 9],
    'October': [31, 10],
    'November': [30, 11],
    'December': [31, 12] 
}
week_m = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wensday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
today_m = [12,'tuesday', 13, 2022]
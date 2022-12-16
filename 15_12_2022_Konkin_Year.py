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
        self.__sum_days = 0
        self.__year_u = None
        self._year_leap = None
        self.__today_d = None
        self.__week_m = None
        self.name_year = None
        self.enter_date = None
    
    @property
    def usualy_year(self):
        return self.__year_u
    @usualy_year.setter
    def usualy_year(self, yr_u):
        self.__year_u = yr_u

    @property
    def leap_year(self):
        return  self._year_leap
    @leap_year.setter
    def leap_year(self, leap):
        self._year_leap = leap

    @property
    def today_day(self):
        return self.__today_d
    @today_day.setter
    def today_day(self, td):
        self.__today_d = td

    @property
    def weeks_day(self):
        return self.__week_m
    @weeks_day.setter
    def weeks_day(self, wd):
        self.__week_m = wd

    def days_in_this_year(self): #how many days in this year and deside what year
        self.enter_date = input('day/month/year:').split('/')
        if int(self.enter_date[2]) % 4 != 0: 
            for m in self.__year_u.values():
                self.__sum_days += m[0]
            self.name_year = self.__year_u
            print('Usually year')
        else:
            for m in self._year_leap.values():
                self.__sum_days += m[0]
            self.name_year = self._year_leap
            print('leap year')
        return self.__sum_days

    def in_which_day_closes_the_new_year(self):
        index = 0
        if int(self.enter_date[2]) == self.__today_d[3] and int(self.enter_date[1] == self.__today_d[0]):
            index = self.__today_d[0]
            print(self.__today_d[0])
        #     days = 0
        #     for m in self.name_year.values():
        #         if index == m[1]:
        #             days = int(m[0])
        # return days

   




    






y_s = Year_self()
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
year_leap = {
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
today_m = [12,'Tuesday', 13, 2022]

y_s.usualy_year = year_us
y_s.leap_year = year_leap
y_s.today_day = today_m
print(y_s.days_in_this_year())
print(y_s.in_which_day_closes_the_new_year())

week_m = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wensday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

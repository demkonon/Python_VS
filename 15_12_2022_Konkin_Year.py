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
        
        self.__year_u = None
        self._year_leap = None
        self.__today_d = None
        self.__week_m = None
        self.name_year = None
        self.dev_galo_days = 0
    
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

    def days_in_this_year(self, year): #how many days in this year and deside what year - warm-up ;-)
        self.enter_date = year
        sum_days = 0
        if int(self.enter_date) % 4 != 0: 
            for m in self.__year_u.values():
                sum_days += m[0]
            self.name_year = self.__year_u
            print('Usually year')
        else:
            for m in self._year_leap.values():
                sum_days += m[0]
            self.name_year = self._year_leap
            print('leap year')
        return sum_days

    def in_which_day_closest_the_new_year(self):
        index = 0
        days = 0
        dop = 0
        user_year = self.enter_date
        if user_year == self.__today_d[3]:
            index = self.__today_d[0]
            for m in self.name_year.values():
                if index == m[1]:
                    days = int(m[0])
                    for key, val in self.__week_m.items():
                        if self.__today_d[1] == val:
                            dop = key
                            self.dev_galo_days = ((days - self.__today_d[2]) % 7) + dop + 1
                        if self.dev_galo_days == key:
                            galo_days = val                  
        return "%s%s" %('Closest New Year - ',galo_days)

    def which_day_some_new_year(self, user_year):
        counter = self.dev_galo_days
        day_holiday = ''
        rayd = user_year - 2022
        for year in range(rayd+1):
            if year != 0:
                year += 2022
                if year % 4 != 0:
                    ostatok = 365 % 7
                elif year % 4 == 0:
                    ostatok = 366 % 7
                counter += ostatok
                if counter <= 7:
                        counter = counter
                elif counter > 7:
                        counter = counter % 7  
        for key, val in self.__week_m.items():
            if key == counter:
                day_holiday = val
        return "%s%s%i" %(day_holiday, ' - the Day of new year this Year - ', user_year)
    
    def day_the_birthday(self, user_year):
        counter = 2
        day_holiday = ''
        rayd = user_year - 1981
        for year in range(rayd+1):
            if year != 0:
                year += 1981
                if year % 4 != 0:
                    ostatok = 365 % 7
                elif year % 4 == 0:
                    ostatok = 366 % 7
                counter += ostatok
                if counter <= 7:
                        counter = counter
                elif counter > 7:
                        counter = counter % 7  
        for key, val in self.__week_m.items():
            if key == counter:
                day_holiday = val
        return "%s%s%i" %(day_holiday, ' - the Day of My Birthday - ', user_year)

        


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
week_m = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wensday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
today_m = [12,'Tuesday', 13, 2022]

y_s.usualy_year = year_us
y_s.leap_year = year_leap
y_s.today_day = today_m
y_s.weeks_day = week_m
print(y_s.days_in_this_year(2022))
print(y_s.in_which_day_closest_the_new_year())

for i in range(2):
    print(y_s.which_day_some_new_year(2023+i))

for i in range(41):
    print(y_s.day_the_birthday(1981+i))
    



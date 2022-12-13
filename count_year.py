from datetime import datetime
import time
import os
def time_couner_ny(et,cor):
    while et > cor:
        time.sleep(1)
        cor = datetime.today()
        print(et - cor)
    return
end_time = datetime(2022, 12, 31)
current_time = datetime.today()
# time_couner_ny(end_time, current_time)


class Timer_self:

    def __init__(self):
        self.__end_time = None

    @property
    def e_time(self):
        return self.__end_time

    @e_time.setter
    def e_time(self,et):
        self.__end_time = et

    def res(self):
        cor = datetime.today()
        while self.__end_time > cor:
            time.sleep(1)
            cor = datetime.today()
            print("\b"*100, self.__end_time - cor, end = '')
            # реализация удаления предыдущего вывода
            os.sys.stdout.flush()

    def res_another(self):
        difference =  self.__end_time - datetime.today()
        sec_days = difference.days * 86400
        sec_days += difference.seconds
        while sec_days > 0:
            time.sleep(1)
            diff = sec_days - datetime.today()
            
            sec_days -= cor_sec
            print("\b"*100, sec_days, end = '')



cor = Timer_self()
cor.e_time = datetime(2022, 12, 31)
# print(cor.res)
print(cor.res_another())
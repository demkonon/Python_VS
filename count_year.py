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
        


cor = Timer_self()
cor.e_time = datetime(2022, 12, 31)
print(cor.res)
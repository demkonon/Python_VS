from datetime import datetime
import time
def time_couner_ny(et,cor):
    while et > cor:
        time.sleep(1)
        cor = datetime.today()
        print(et - cor)
    return
    
end_time = datetime(2022, 12, 31)
current_time = datetime.today()

time_couner_ny(end_time, current_time)
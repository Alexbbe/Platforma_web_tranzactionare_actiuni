from datetime import datetime,time

def is_time_between():
    check_time = datetime.now().time()
    begin_time = time(16,30,0)
    end_time = time(23,0,0)
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:
        return check_time >= begin_time or check_time <= end_time

def is_weekend():
    weekno = datetime.today().weekday()
    if weekno < 5:
        return False
    else:
        return True


x = is_time_between()
print(x)
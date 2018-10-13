import time
current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
month = current_time.tm_mon
year = current_time.tm_year
day = current_time.tm_mday

print("Date: ",day,".",month,".",year)
print("Time: ",hour,":",minute)

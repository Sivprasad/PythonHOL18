import time
import snaps
current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min

if (hour > 7) or (hour == 7 and minute > 29):
    snaps.display_message("TIME TO GET UP")
    snaps.play_sound("alarm.wav")
    time.sleep(10)
print("The time is", hour, ":", minute)

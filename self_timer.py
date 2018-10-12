import random
import time

print("Welcome to Self Timer")
print()
print("Everybody stand up")
print("Stay standing until you think the time has ended")
print("Then sit down.")
print("Anyone still standing when the time ends loses. ")
print("The last person to sit down before the time edned will win")

stand_time = random.randint(5,20)
print("Stay stands for ",stand_time," seconds.")
time.sleep(stand_time)
print("*****TIME UP*****")

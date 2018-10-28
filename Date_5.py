import datetime
##today is a function that return tody's date
currentDate = datetime.date.today()
##print(currentDate.year, end = " ")
##print(currentDate.month,end=" ")
##print(currentDate.day, end =" ")
##strftime allwos you to special the date format 
#print(currentDate.strftime('%d ,%b,%y'))

userInput = input("Pleae enter your birthday")
birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
print(birthday)
days = birthday - currentDate
print(days.days)
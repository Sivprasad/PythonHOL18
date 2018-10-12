##1 Program displays a number between 1 and 10, inclusively,
##2 The program then sleeps for 20 seconds while the program
##  sleep, the players are invide to decide whether the nex number will
##  be higher or lower than the number just printed, Player who choose "high"
##  stands on right side, player who choose "low" stands on left
##
##3) The program then display a second number between 1 and 10 , and anyone who
##   was wrong  is eliminated from the game. the program is then re-run  with the playersthat are left until you have a winner 
##
##
##Created by Sivaprasad. G
import random
import time

print("The Number is : ",random.randint(1, 10))
num = random.randint(1, 10)
guessNum = input("Guess the next number: ")
print("Hmm let me check ....")
time.sleep(10)
if int(guessNum )== int (num) :
   print("The number is ",num,"congrats  have right guess" )
else:
    print("The number is ",num,"and you lost!")

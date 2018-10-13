import snaps
snaps.display_image('themepark.png')
print("\t\t\t Welcome to our Theme Park\t\t\t")
print("\n\nThese are the avilable rides: \n")
print("1. cenic River Cruise\n")
print("2. Carnival Carousel\n")
print("3. Jungle Adventur Water Splash\n")
print("4. Downhill Mountain Run\n")
print("5. The Regurgitator\n")

choice = input("Please enter the ride number you want: ")
ride_number = int(choice)
if ride_number == 1:
        print("You have selected the Scenic River Cruise")
        print("There are no age limits for this ride")
else:
        age_txt = input("Pleae enter you age: ")
        age = int(age_txt)

if ride_number == 2:
   print("You have selected Carnival Carousel")
   if age >= 3:
           print("You can go on the ride.")
   else:
           print("Sorry, You are too young.")
           
if ride_number == 3:
        print("You have selected Jungle Adventur Water Splash")
        if age >= 6:
                print("You can go on the ride.")
        else:
                print("Sorry, You are too young.")

if ride_number == 4:
        print("You have selected Downhill Mountain Run")
        if age >= 9:
                print("You can go on the ride.")
        else:
                print("Sorry, You are too young.")

if ride_number == 5:
        print("You have selected The Regurgitator")
        if age >= 12:
                if age > 70:
                        print("Sorry, You are too old.")
                else:
                        print("You can go on the ride.") 
else:
        print("Sorry, You are too young.")


                
                
        
        
           


                
        
        
           

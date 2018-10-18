try:
    ride_number_text =  input("Please enter the ride number you want ")
    ride_number = int(ride_number_text)
    print("You have enterd",ride_number)
except ValueError:
    print("Invalid number")
 

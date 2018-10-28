#fileName = "GuestList.csv"
#WRITE = "w"
 
#myFile = open(fileName,mode = WRITE)
#myFile.write("Hi there! line No, 1 \n")
#myFile.write("How are you! line No, 2")
#myFile.close()
fileName = "GuestList.txt"
WRITE = "w"
data = input("Please enter file info ")
file = open(fileName, mode = WRITE)
file.write(data)
file.close()
print("File writtern successfully")
import csv
#cityList = ["Seattle", "London", "Paris", "Sydney"]
#cityList.remove("Seattle")
 #animalFile = open("textmania.txt","r")
#firstAnimal = animalFile.readline()
#print(firstAnimal)
##secondAnimal = animalFile.readline()
##print(secondAnimal)
###read all file contents
##allFileContents = animalFile.read()
##print(allFileContents)
with open ("textmania.txt","r") as animalFile :
	allRowsList = csv.reader(animalFile)
	
	for currentRow in allRowsList:
		print(currentRow)
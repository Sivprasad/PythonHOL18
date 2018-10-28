#guests = [ "Christopher","Susan","Satya","Bill" ] 

#print ("First value is ", guests[0])
#print (guests[1])
#guests[0] = "Steve"
#print("first valu is now "+guests[0])
#guests.remove('Steve')
#print("first valu now "+guests[0])
#del guests[0]
#print("first value now "+guests[0])
#guests.append('Colin')
#print(guests[2])
#print(guests.index('Bill'))
guests = [ "Christopher","Susan","Satya","Bill" ] 
for guest in guests:
	guests = guests.remove(guest)
	
print(guests)
 
# python list are containers to store a set of any data types
# A list can be indexed just like a string.
# list is a fully flexible , we can change or add something because it is mutbale.
friends=["Apple","Orange",5,56.76,False,"Aakash","Rohan"]
print(friends[0])

friends[0]="Grapes"
print(friends[0]) #list is mutable it will change 
                  #but string is immutable, can't change.

friends[3]=34
print(friends[3])

friends[5]="nkg"
print(friends[5])

print(friends[1:5])  #1 is included and 4 is excluded

print(friends[:5])
print(friends[0:])  #i.e means 0:length

print(friends[5:])   #i.e means 5:length 

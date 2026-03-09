friends=["Apple","Orange",5,45.65 , False, "Aakash","Rohan"]  #always first letter of True & False will be capital
print(friends)

     #Append method
print("append method")
friends.append("Nitish")  #append means at the end stick
print(friends)

      #short method
print("short method")
l1=[1,34,62,2,6,11]
l1.sort()   #sort means sequence increasing
print(l1)

      #reverse method
print("reverse method")
l1.reverse()
print(l1)

l2=[1,34,62,2,6,11]
l2.reverse()
print(l2)

       #insert method
print("insert method")

l3=[1,34,62,2,6,11]
l3.insert(3,333)   #(index,no. what you add)
print(l3)
       #pop method 
print("pop method")

l4=[1,34,62,2,6,11]
l4.pop(3)
print(l4)

l5=[1,34,62,2,6,11]

print(l5.pop(3))   # we can write also - value=l5.pop(3) ---  print(value)   return 2 hi krega

       #remove method
print("remove method")
l6=[1,34,62,2,6,11]
l6.remove(34)
print(l6)

        #clear method
print("clear method")
l7=[1,34,62,2,6,11]
l7.clear()
print(l7)

name="harry"

print(name[-4:-1])   #-1 is not included
print(name[1:4])  #convert -ve index into positive index

print(name[:4])  #is same as print(name[0:4])
print(name[1:])  #is same as prit(name([1:5])) ,where 5 is the length(5)
print(name[1:5])
 
nameshort=name[0:3]  #3 is not included
print(nameshort)

nameshort=name[1:3]
print(nameshort)
character1=name[1]  #indexing         # "  H  A  R  R  Y"
print(character1)                     #    0  1  2  3  4
                                      #   -5 -4 -3 -2 -1

character2=name[-4]
print(character2)

character3=name[-5]
print(character3)


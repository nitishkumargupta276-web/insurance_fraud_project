# operator are symbols that perform operation.
# types of operator
''' 1.arithmatic operator :=,-,*,/,etc.
    2.assignment operator :=,+=,-=,etc.
    3.comparison operators:==,>,>=,<,!=,etc.
    4.logical operator:and ,or,not.'''

     #eg-7+4=11 (7&4 are operands,+is an operator,&11 is a result).


    #   ARITHMATIC OPERATOR
x="arithmatic operator"
print(x)
a=8
b=7
print(a+b,a-b,a*b,a/b,a//b,a%b)
print(a/b)

     #  ASSIGNMW=ENT OPERATOR
x="assignment opeator"
print(x)
a=4-2  #assign 4-2 in a
print(a)
b=6
b-=8

b+=3  #increment the value of b by 3 and then assign it to b
print(b) 
b-=3  #decrement the value of b by 3 and then assign it to b
print(b)


    #COMPARISON OPERATOR always return boolean(T/F)
x="comparison opeator"
print(x)
d=5>4
print(d)
e=8<3
print(e)
f=5==5
print(f)
g=5>5
print(g)
h=5<=5
print(h)
i=5!=5  #!= is not equal to
print(i)



    #LOGICAL OPERATOR

z="logical operator"
print(z)

p=True or False
print(p)
#truth table of or
print("true or false is",True or False)
print("true or true is",True or True)
print("false or false is",False or False)

#truth table of and
print("\n")
print("true and false is",True and False)
print("true and true is",True and True)
print("false and false is",False and False)

print(not(True))  #not operator
print(not(False))
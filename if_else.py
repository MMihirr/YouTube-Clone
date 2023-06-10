# Simple if 

x = 10 

if (x==10):
    print("good")

# Dynamic if_else
'''
a = int(input("Enter A No : "))
b = int(input("Enter B No : "))

if a>b:
    print("A is Bigger")
else:
    print("B is Bigger")'''

age = int(input("Enter your age : "))

if age>=18:
    wit = int(input("Enter your weight : "))
    if wit>=50:
        print("You can Donate")
    else:
        print("Under Weight")
else:
    print("Under Age")
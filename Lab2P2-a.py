import math

def check_if_valid():
    while True:
        try:
            var=float(input("Please give me the diameter of a circle. Decimals are accepted: "))
        except ValueError:
            print("That is not a number, please try again.")
        else:
            return var

def circum(a):
    return math.pi*a

def area(a):
    return math.pi*((a**2)/2)

x=check_if_valid()

<<<<<<< HEAD
print("The circumference of the circle is {0}".format(round(circum(x),2)))
print("The area of the circle is {0}".format(round(area(x),2)))
=======
print("The circumference of the circle is: " + str(circum(x)))
print("The area of the circle is: " + str(area(x)))
>>>>>>> ca52a16fe01ae2a839c77a24d96f2c8c13c511f3

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

print("The circumference of the circle is {0}".format(round(circum(x),2)))
print("The area of the circle is {0}".format(round(area(x),2)))
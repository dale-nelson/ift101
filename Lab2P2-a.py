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

print("The circumference of the circle is: " + str(circum(x)))
print("The area of the circle is: " + str(area(x)))
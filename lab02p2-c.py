import math

def check_if_valid():
    while True:
        try:
            val=float(input())
        except ValueError:
            print("That is not a number, please try again.")
        else:
            return val

def positive(a,b,c,d):
    return (-b+math.sqrt(d))/(2*a)

def negative(a,b,c,d):
    return (-b-math.sqrt(d))/(2*a)

def part_one(a,b,c):
    d = (b**2)-(4*a*c)
    return d

print("Please enter the value for a: ")
x=check_if_valid()

print("Please enter the value for b: ")
y=check_if_valid()

print("Please enter the value for c: ")
z=check_if_valid()

w = part_one(x,y,z)

if w < 0:
<<<<<<< HEAD
    print("Unfortunately, your 3 numbers cause a negative number to appear under the \nsquare root of the quadratic formula which results in imaginary or complex numbers.")
=======
    print("Unfortunately, your 3 numbers cause a negative number to appear under the square root of the quadratic formula which results in imaginary or complex numbers.")
>>>>>>> ca52a16fe01ae2a839c77a24d96f2c8c13c511f3
else:
    if x == 0:
        print("'a' cannot be 0, otherwise it is division by 0.")
    else:
<<<<<<< HEAD
        print("The solutions for x are {0} and {1}".format(round(positive(x,y,z,w),3),round(negative(x,y,z,w),3)))
=======
        print("The solutions for x are {0} and {1}".format(positive(x,y,z,w),negative(x,y,z,w)))
>>>>>>> ca52a16fe01ae2a839c77a24d96f2c8c13c511f3

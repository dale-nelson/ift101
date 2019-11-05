import time
time_val = time.time()

print("This program will compute the perimeter and area of a rectangle.")
time.sleep(1)

def check_if_valid():
    while True:
        try:
            var=float(input("Please enter a number. Decimals are also accepted: "))
        except ValueError:
            print("That is not a number, please try again.")
        else:
            return var

def perimeter(a,b):
    return 2*(a+b)

def area(a,b):
    return a*b

x=check_if_valid()
y=check_if_valid()

print("The perimeter of the rectangle is: " + str(perimeter(x,y)))
print("The area of the rectangle is: " + str(area(x,y)))

print("This program took {0} seconds to run.".format(round(time.time() - time_val,2)))